from frontend_py.token.token import Token
EOF = -1

class Base_Lexer:
    def __init__(self):
        self.line = ""
        self.pos = 0
        self.tokens = []

    def get_next_token(self) -> Token:
        if self.pos == len(self.line):
            return Token("EOF", "-1")

        letter = self.get_char()

        if self.is_r_curly_br(letter):
            self.advance()
            return Token("PROGRAM_EXIT", "}")
        else:
            self.advance()
            return Token("BASE_PROGRAM", "NULL")

    def is_r_curly_br(self, letter):
        if letter == '}':
            return True
        return False

    def get_char(self):
        if self.pos < len(self.line):
            return self.line[self.pos]
        return EOF

    def advance(self):
        self.pos += 1