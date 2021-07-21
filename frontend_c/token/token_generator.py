modes = {"tex": 0, "math": 1, "base": 2}


class TokenScanner:
    def __init__(self, token_fp, type):
        self.token_fp = token_fp
        self.token_c_fp = f"{type}_tokens.c"
        self.token_h_fp = f"{type}_tokens.h"
        self.type = type
        self.tokens = []
        self.terminal_names = {}

    # Run self.scan_token_file
    # Run self.scan_terminal_file

    def scan_token_file(self):
        # Loop over the file lines and collect the tokens and their siblings using the tokens class below.
        with open(self.token_fp) as f:
            lines = f.readlines()
        i = 0
        while i < len(lines):
            # Find the first non blank line
            while i < len(lines):
                if (curr_line := lines[i].strip()) == "":  # Skip blank lines
                    i += 1
                else:
                    break
            # Find the second non blank line, if possible:
            next_line = ""
            while i < len(lines) - 1:
                if (next_line := lines[i + 1].strip()) == "":
                    i += 1
                else:
                    break
            # At this point we have curr_line and next_line with token data
            token_name, token_value = get_token_data(curr_line)
            curr_token = Token(token_name, token_value, modes[self.type])
            self.tokens.append(curr_token)
            if is_sibling_statement(next_line):
                sibling_name, sibling_value = get_token_data(next_line)
                curr_token.sibling = Token(
                    sibling_name, sibling_value, modes[self.type]
                )
                # i += 1
            i += 1

    def scan_terminal_file(self, terminal_fp: str) -> None:
        # Scan the terminals file and create a correspondence between terminals and positive integers.
        macro_stmts = []
        with open(terminal_fp) as f:
            for line in f.readlines():
                line_entries = line.split()
                if len(line_entries) != 2:
                    raise SyntaxError(
                        f"Too many or too few line entries for a terminal: {line}"
                    )
                terminal_name = line_entries[0]
                terminal = line_entries[1]
                terminal_val = hash(terminal_name)

                # Update the terminal dictionary with the terminal name
                self.terminal_names[terminal] = terminal_name
                terminal_macro = f"#define {terminal_name} {terminal_val} \n"
                macro_stmts.append(terminal_macro)

        with open("token_values.h", "w") as f:
            f.write("// Auto-generated from token_generator.py\n")
            f.write("#ifndef TEX_COMPILER_TOKEN_VALUES_H\n")
            f.write("#define TEX_COMPILER_TOKEN_VALUES_H\n")
            f.write(
                """
const unsigned long hash(const char *str) { 
    // Excellent hash function known as djb2.
    unsigned long hash = 5381;  
    int c;

    while (c = *str++)
        hash = ((hash << 5) + hash) + c;
    return hash;
}\n
"""
            )
            f.writelines(macro_stmts)
            f.write("#endif //TEX_COMPILER_TOKEN_VALUES_H\n")

    def write_token_files(self):
        # Create the .c and .h token files containing function definitions.
        token_func_defns = []
        token_declarations = []
        token_c_preamble = f"""\
// Auto-generated from token_generator.py
#include <stdlib.h> 
#include <stdio.h>   
#include <string.h>
#include "{self.type}_tokens.h"  
#include "token.h"\n
"""
        token_h_preamble = """\
// Auto-generated from token_generator.py
#ifndef TEX_COMPILER_TOKEN_H
#define TEX_COMPILER_TOKEN_H
#include "token.h"\n\n
"""
        # Now we loop over the tokens and write their functions
        for token in self.tokens:
            declaration = f"Token new_{token.name.lower()}_token(void);\n\n"
            if token.sibling is not None:
                sibling_line = (
                    f"{token.name}->sibling = new_{token.sibling.name.lower()}_token();"
                )
            else:
                sibling_line = ""
            token_value = token.value.replace("\\", "\\\\")
            token_C_template = f"""\
Token new_{token.name.lower()}_token(void){{
    Token {token.name} = malloc(sizeof *{token.name});
    if ({token.name} == NULL){{
        printf("Memory allocation for {token.name} token failed");
        return NULL;
    }}
    {token.name}->name  = strdup("{token.name}");
    {token.name}->value = strdup("{token_value}");
    {token.name}->type  = {token.type};
    {sibling_line}
    return {token.name};
}}\n
"""  # Append the function definition
            token_declarations.append(declaration)
            token_func_defns.append(token_C_template)

        # Write the header file with our declarations
        with open(self.token_h_fp, "w") as f:
            f.write(token_h_preamble)
            f.writelines(token_declarations)
            f.write("#endif //TEX_COMPILER_TOKEN_VALUES_H\n")

        # Write the .c file with our definitions
        with open(self.token_c_fp, "w") as f:
            f.write(token_c_preamble)
            f.writelines(token_func_defns)

    def write_lexer_files(self):
        # Requires running self.terminal_scanner first
        lexer_c_fp = f"../lexer/{self.type}_lexer.c"
        lexer_h_fp = f"../lexer/{self.type}_lexer.h"
        # Tokens beginning with a backslash
        backslash_token_stmts = []
        backslash_token_switch = """\
    if (strcmp(curr_char, "\\\\"))
        switch (hash(lookahead)){
"""
        # Tokens with two characters
        two_char_token_stmts = []
        # Tokens with one character
        single_char_token_stmts = []
        single_token_switch = """\
    switch(hash(curr_char)){   
"""
        # Template for the lexer file
        lexer_template = f"""\
// Auto-generated by lexer_generator.py
#include <stdio.h>
#include <token.h>
#include <token_values.h>
#include "{self.type}_lexer.h"
#include <{self.type}_tokens.h>


Token get_next_token(char first_char, char second_char){{
    char *curr_char;
    char *lookahead;
    strcpy(curr_char, first_char);
    strcpy(lookahead, second_char);

    if (is_blank(curr_char))
        return skip_blanks();

    if (isalpha(curr_char))
        return get_word();

    // Backslash tokens

    // Two character tokens

    // Single character tokens

}}

"""
        # Loop over the tokens and create the C statements necessary for the get_next_token function.
        for token in self.tokens:
            if token.value is None:
                continue
            nchars = len(token.value)
            # Single character tokens
            if nchars == 1:
                c_code = match_one_char(token.name, self.terminal_names[token.value])
                single_char_token_stmts.append(c_code)
            # Two character tokens
            elif nchars == 2:
                # Backlash tokens
                if token.value[0] == "\\":
                    c_code = match_backslash_and_char(
                        token.name, self.terminal_names[token.value[1]]
                    )
                    backslash_token_stmts.append(c_code)
                # Other two character tokens
                else:
                    c_code = match_two_chars(token.name, token.value[0], token.value[1])
                    two_char_token_stmts.append(c_code)
            else:
                raise SyntaxError(
                    f"Too many characters ({nchars}) in the token value: {token.value}"
                )

        # We write our C statements in the lexer C file.
        with open(lexer_c_fp, "w") as f:
            lexer_lines = lexer_template.split("\n")
            for line in lexer_lines:
                f.write(line + "\n")
                if (
                    len(line_entries := line.split()) > 0
                ):  # Check if the line is nonempt
                    if line_entries[0] == "//":
                        first_word = line_entries[1]
                        if first_word == "Backslash":
                            f.write(backslash_token_switch)
                            f.writelines(backslash_token_stmts)
                            # Add a default statement
                            f.write("       }")
                        elif first_word == "Two":
                            f.writelines(two_char_token_stmts)
                        elif first_word == "Single":
                            f.write(single_token_switch)
                            f.writelines(single_char_token_stmts)
                            f.write("   }")
        # We also write the lexer h file.
        with open(lexer_h_fp, "w") as f:
            f.write(
                f"""\
#ifndef TEX_COMPILER_{self.type.upper()}_LEXER_H
#define TEX_COMPILER_{self.type.upper()}_LEXER_H

#include "../Token/token.h"

Token get_next_token(char first_char, char second_char);

#endif //TEX_COMPILER_{self.type.upper()}_LEXER_H
            """
            )


class Token:
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type
        self.sibling = None


def is_sibling_statement(next_line: str) -> bool:
    # Check if the line contains a "sibling:" call
    if next_line == "":
        return False
    elif next_line.split()[0] == "sibling:":
        return True
    else:
        return False


def get_token_data(line: str) -> tuple:
    # Extract the token name and token value from a line and return the values
    line_entries = line.split()
    n_entries = len(line_entries)

    if n_entries == 1:
        return line_entries[0], None
    if n_entries == 2:
        return line_entries[0], line_entries[1]
    if n_entries == 3:
        if line_entries[0] == "sibling:":
            return line_entries[1], line_entries[2]
        else:
            raise SyntaxError(
                f'Unknown keyword {line_entries[0]}; expecting "sibling:"'
            )
    else:
        raise SyntaxError(f"Too many values: {line}")


def hash(string):
    # Calculates the hash value of a string. Also known as djb2.
    hash_val = 5381

    for char in string:
        hash_val = ((hash_val << 5) + hash_val) + ord(char)

    return hash_val


def match_one_char(token_name, macro_name):
    c_code = f"""\
        case {macro_name}:
            return new_{token_name.lower()}_token();
"""
    return c_code


def match_two_chars(token_name, char, next_char):
    c_code = f"""\
    if (strcmp(curr_char, "{char}") && strcmp(lookahead, "{next_char}")
        return new_{token_name.lower()}_token();
"""
    return c_code


def match_backslash_and_char(token_name, macro_name):
    c_code = f"""\
            case {macro_name}:
                return new_{token_name.lower()}_token();
"""
    return c_code
