from frontend_py.token.token import Token
EOF = -1

# We need three different lexical analyzers.
#   1. A TeX lexer, which interprets the source for TeX syntax.
#   2. A Math lexer, which interprets the source for in-line and display math syntax.
#   3. A base program lexer, which interprets the source for base program syntax.
# The parser is in charge of swapping out the different lexers, based on the tokens it receives.
# For example, if it is in the TeX lexer and it sees a non-escaped {, it will switch to the
# base program lexer until it finds a matching, unbalanced } token.

class TeX_Lexer():
    def __init__(self):
        self.line = ""
        self.pos = 0

    def get_next_token(self) -> Token:
        if self.pos == len(self.line):
            return Token("EOF", "-1")
        letter = self.get_char()
        # Ignore white space
        if self.is_blank(letter):
            return self.get_blanks()

        # Check if the start is a letter
        elif self.is_letter(letter):
            return self.get_word()

        # Check if the start is a dollar
        elif letter == '$':
            self.advance()
            # Check if it is a double dollar
            letter = self.get_char()
            if letter == '$':
                self.advance()
                return Token("DBL_DOLLAR", "$$")
            return Token("DOLLAR", "$")

        # Check if the start is backslash
        elif letter == '\\':
            # We must expect one of the following tokens:
            #   1. ( token => beginning inline math.
            #   2. [ token => beginning display math.
            #   3. Escape character token
            #   4. Try to extract an identifier token.
            #       If success, then we expect
            #           1. A ( token => identifier is a function. Switch to base language lexer to evaluate arguments.
            #           2. A { token => identifier is a control sequence. Keep using TeX lexer.
            #           3. A space token => identifier is a variable. Continue scanning
            #   5. Else, we have a syntax error
            self.advance()
            next = self.get_next_token().string
            if next == '(':
                return Token("L_IL_MATH", "\\(")
            elif next == '[':
                return Token("L_DP_MATH", "\\[")
            elif next == ')':
                return Token("R_IL_MATH", "\\)")
            elif next == ']':
                return Token("R_DP_MATH", "\\]")
            elif next == '{':
                return Token("ESC_LBRACE", "\\{")
            elif next == '}':
                return Token("ESC_RBRACE", "\\}")
            elif next == '\\':
                return Token("NEWLINE", "\\\\")
            elif next == ' ':
                print("Syntax Error: Lonely \\")
            else:
                return Token("BACKSLASH", "\\")

        # Check if the start is a curly brace
        elif letter == '{':
            self.advance()
            return Token("LBRACE", "{")

        elif letter == '}':
            self.advance()
            return Token("RBRACE", "}")

        elif letter == '[':
            self.advance()
            return Token("LSQB", "[", )

        elif letter == ']':
            self.advance()
            return Token("RSQB", "]")

        elif letter == '(':
            self.advance()
            return Token("LPAR", "(")

        elif letter == ')':
            self.advance()
            return Token("RPAR", ")")

        else:
            return f"Unrecognized character {letter}"

    # Ignore the whitespace, but make note of spaces and newlines
    def get_blanks(self):
        # Outputs either one space token or one new line token
        # Upon exit, self.pos corresponds to the index of the first non-blank character that comes after our initial
        # blank.
        space_tok, newline_tok = None, None
        seen_a_space = False
        while self.is_blank(next := self.get_char_and_advance()):
            if next == '\n':
                newline_tok = Token("EOL", "\n")
                break
            elif not seen_a_space:
                if next == ' ':
                    space_tok = Token("SPACE", " ")
                    seen_a_space = True
        if newline_tok is not None:
            return newline_tok
        else:
            self.backtrack()
            return space_tok

    # Get word in sentence
    def get_word(self):
        # Upon exit, this leaves self.pos to the first non-letter character seen after getting the word
        word = ""
        while self.is_letter(next := self.get_char_and_advance()) and next != EOF:
            word += next
        if next != EOF:
            self.backtrack()
        return Token("WORD", word)

    def is_blank(self, letter):
        return letter == ' ' or letter == '\t' or letter == '\n'

    def is_letter(self, letter):
        if isinstance(letter, str):
            return letter.isalpha()
        return False

    # The methods to advance our position
    def advance_and_get_char(self):
        if self.pos < len(self.line) - 1:
            self.pos += 1
            return self.line[self.pos]
        return EOF

    def get_char_and_advance(self):
        if self.pos < len(self.line):
            next = self.line[self.pos]
            self.pos += 1
            return next
        return EOF

    def get_char(self):
        if self.pos < len(self.line):
            return self.line[self.pos]
        return EOF

    def advance(self):
        self.pos += 1

    def backtrack(self):
        self.pos -= 1


