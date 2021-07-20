modes = {"tex": 0, "math": 1, "base": 2}


class TokenScanner:
    def __init__(self, token_fp, type):
        self.token_fp = token_fp
        self.token_c_fp = f"{type}_tokens.c"
        self.token_h_fp = f"{type}_tokens.h"
        self.type = type
        self.tokens = []

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
                if (next_line := lines[i+1].strip()) == "":
                    i += 1
                else:
                    break
            # At this point we have curr_line and next_line with token data
            token_name, token_value = self.get_token_data(curr_line)
            curr_token = Token(token_name, token_value, modes[self.type])
            self.tokens.append(curr_token)
            if self.is_sibling_statement(next_line):
                sibling_name, sibling_value = self.get_token_data(next_line)
                curr_token.sibling = Token(sibling_name, sibling_value, modes[self.type])
                # i += 1
            i += 1

    def write_token_files(self):
        # Create the tokens .c and .h file.
        token_func_defns = []
        token_declarations = []
        token_c_preamble =\
"""// Auto-generated from token_generator.py
#include <stdlib.h> 
#include <stdio.h>   
#include <string.h>
#include "tex_tokens.h"  
#include "token.h"\n
"""
        token_h_preamble =\
"""// Auto-generated from token_generator.py
#ifndef TEX_COMPILER_TOKEN_VALUES_H
#define TEX_COMPILER_TOKEN_VALUES_H
#include "token.h"\n\n
"""
        # Now we loop over the tokens and write their functions
        for token in self.tokens:
            declaration = f"Token new_{token.name.lower()}_token(void);\n\n"
            if token.sibling is not None:
                sibling_line = f"{token.name}->sibling = new_{token.sibling.name.lower()}_token();"
            else:
                sibling_line = ""
            token_C_template =\
f"""
Token new_{token.name.lower()}_token(void){{
    Token {token.name} = malloc(sizeof *{token.name});
    if ({token.name} == NULL){{
        printf("Memory allocation for {token.name} token failed");
        return NULL;
    }}
    {token.name}->name  = strdup("{token.name}");
    {token.name}->value = strdup("{token.value}");
    {token.name}->type  = {token.type};
    {sibling_line}
    return {token.name};
}}\n
"""         # Append the function definition
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


    def is_sibling_statement(self, next_line):
        if next_line == "":
            return False
        elif next_line.split()[0] == "sibling:":
            return True
        else:
            return False

    def get_token_data(self, line):
        line_entries = line.split()
        n_entries = len(line_entries)

        if n_entries == 1:
            return line_entries[0], None
        if n_entries == 2:
            return line_entries[0], line_entries[1].replace("\\", "\\\\") # Escape \ for C
        if n_entries == 3:
            if line_entries[0] == "sibling:":
                return line_entries[1], line_entries[2].replace("\\", "\\\\")
            else:
                raise SyntaxError(f"Unknown keyword {line_entries[0]}; expecting \"sibling:\"")
        else:
            raise SyntaxError(f"Too many values: {line}")


def terminal_scanner(terminal_fp: str) -> None:
    macro_stmts = []
    with open(terminal_fp) as f:
        for ind, line in enumerate(f.readlines()):
            line_entries = line.split()
            n_entries = len(line_entries)

            if n_entries != 2:
                raise SyntaxError(f"Too many or too few line entries for a terminal: {line}")
            macro_stmt = f"#define {line_entries[0]} {ind} \n"
            macro_stmts.append(macro_stmt)

    with open("token_values.h", "w") as f:
        f.write("// Auto-generated from token_generator.py\n")
        f.writelines(macro_stmts)

class Token:
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type
        self.sibling = None

