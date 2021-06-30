from frontend_py.token.token import Token
EOF = -1

class Math_Lexer:
    def __init__(self):
        self.line = ""
        self.pos = 0
        self.expect = []

    def get_next_token(self):
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
        elif letter == "$":
            self.advance()
            # Check if it is a double dollar
            next = self.get_char()
            if next == '$':
                self.advance()
                return Token("STOP_DBL_DOLLAR", "$$")
            return Token("STOP_DOLLAR", "$")

        # Check if the start is backslash
        elif letter == '\\':
            self.advance()
            next = self.get_char()
            if next == '{':
                self.advance()
                return Token("L_SET_BRACE", "\\{")
            elif next == '}':
                self.advance()
                return Token("R_SET_BRACE", "\\}")
            elif next == '\\':
                self.advance()
                return Token("NEWLINE", "\\\\")
            elif next == ' ':
                self.advance()
                print("Syntax Error: Lonely \\")
            elif next == ')':
                self.advance()
                return Token('STOP_INL_MATH', "\\)")
            elif next == ']':
                self.advance()
                return Token('STOP_DSP_MATH', "\\]")
            else:
                return Token("BACKSLASH", "\\")

        elif letter == '_':
            self.advance()
            next = self.get_char()
            if next == '{':
                self.expect_tok("E_SUB_GRP", "}")  # Implement this with a stack.
                self.advance()
                return Token("B_SUB_GRP", "_{")
            return Token("SUB", "_")

        elif letter == '^':
            self.advance()
            next = self.get_char()
            if next == '{':
                self.expect_tok("E_SUP_GRP", "}")
                self.advance()
                return Token("B_SUP_GRP", "^{")
            return Token("SUP", "^")

        elif letter == '&':
            self.advance()
            return Token("ALIGN", "&")

        # Check if the start is a curly brace
        elif letter == '{':
            self.advance()
            return Token("LBRACE", "{")

        elif letter == '}':
            self.advance()
            if len(self.expect) != 0:
                tok_name, tok_type = self.expect.pop()
                return Token(tok_name, tok_type)
            return Token("RBRACE", "}")

        elif letter == '[':
            self.advance()
            return Token("LSQB", "[", )

        elif letter == ']' :
            self.advance()
            return Token("RSQB", "]")

        elif letter == '(':
            self.advance()
            return Token("LPAR", "(")

        elif letter == ')':
            self.advance()
            return Token("RPAR", ")")

        else:
            self.advance()
            print(f"Unrecognized character {letter}")

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

    # Append a token which we expect to see later.
    def expect_tok(self, tok_name, tok_value):
        self.expect.append((tok_name, tok_value))

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

