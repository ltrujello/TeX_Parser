from frontend_py.token.token import Token
from frontend_py.parser.base_parser import Base_Parser
from frontend_py.parser.tex_parser import TeX_Parser
from frontend_py.parser.math_parser import Math_Parser

class Parser:
    def __init__(self):
        self.line = ""
        self.pos = 0
        self.tokens = []
        self.expected_tokens = []

        self.base_parser = Base_Parser()
        self.tex_parser = TeX_Parser()
        self.math_parser = Math_Parser()

        self.cur_tok = Token("", "")
        self.mode = 'TeX'  # Initial state
        self.stop_scan = ""  # Helps break out of and transition to different parsers

    # XXX Need to be able to recognize numbers and additional characters
    def parse(self):
        while not self.match_cur_tok('EOF'):
            print("PASS", self.mode)
            if self.mode == 'TeX':
                self.cur_tok = self.parse_tex()
                if self.match_cur_tok('EOF'):
                    break
                # Update position before transitioning to another state
                self.pos = self.tex_parser.tex_lexer.pos
                self.tex_transition()

            elif self.mode == 'Math':
                self.cur_tok = self.parse_math()  # Stopped and return because we found the stop scan token
                if self.match_cur_tok('EOF'):
                    break
                self.pos = self.math_parser.math_lexer.pos
                self.math_transition()

            elif self.mode == 'BaseLanguage':
                self.cur_tok = self.parse_base_lang()  # Stopped and returned because we found a TeX token
                if self.match_cur_tok('EOF'):
                    break
                self.pos = self.base_parser.base_lexer.pos
                self.base_transition()

            else:
                print(f"Unknown mode {self.mode}")
                break

    def parse_tex(self):
        return self.tex_parser.parse(self.line, self.pos)  # Stopped/returned because we found a foreign token

    def parse_math(self):
        return self.math_parser.parse(self.line, self.pos, self.stop_scan)

    def parse_base_lang(self):
        return self.base_parser.parse(self.line, self.pos, self.stop_scan)

    def tex_transition(self):
        self.mode = self.cur_tok.type
        self.stop_scan = self.cur_tok.sibling
        self.expected_tokens.append(self.cur_tok.sibling)

    def math_transition(self):
        if self.match_cur_tok('LBRACE'):
            self.mode = 'BaseLanguage'
            self.stop_scan = Token('PROGRAM_EXIT', "}")
        else:
            self.mode = 'TeX'
            self.stop_scan = Token('EOF', "-1")

    def base_transition(self):
        self.mode = 'TeX'
        self.stop_scan = Token("EOF", "-1")

    def match_next_token(self, token_str) -> bool:
        return self.cur_tok.name == token_str

    def match_cur_tok(self, token_str) -> bool:
        if self.cur_tok.name == token_str:
            self.add_token(self.cur_tok, self.cur_tok.name)
            return True
        return False

    def add_token(self, token, string):
        self.tokens.append((token, string))