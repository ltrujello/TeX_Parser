from frontend_py.lexer.tex_lexer import TeX_Lexer

#   Possible syntax transitions
#   Tex Mode      -> Base Language
#                 -> Math mode
#
#   Base Language -> Tex Mode
#
#   Math Mode     -> Tex Mode
#                 -> Base Language

class TeX_Parser:
    def __init__(self):
        self.tex_lexer = TeX_Lexer()

    def parse(self, line, pos):
        self.tex_lexer.line = line
        self.tex_lexer.pos = pos
        while True:
            self.cur_tok = self.tex_lexer.get_next_token()
            print("TeX Token:", self.cur_tok)
            if self.match_cur_tok('EOF'):
                return self.cur_tok
            # A space token
            if self.match_cur_tok('SPACE'):
                self.add_token("SPACE", ' ')

            # A word token
            elif self.match_cur_tok('WORD'):
                self.add_token("WORD", self.cur_tok.value)

            # Program access
            elif self.match_cur_tok('LBRACE'):
                # TeX Mode -> Base Language
                return self.cur_tok

            # A new line
            elif self.match_cur_tok('NEWLINE'):
                continue

            # Start of a series of math tokens
            elif self.match_cur_tok('DOLLAR'):
                # TeX Mode -> Math Mode
                return self.cur_tok

            elif self.match_cur_tok('DBL_DOLLAR'):
                # TeX Mode -> Math Mode
                return self.cur_tok

            # Tokens beginning with a backslash
            elif self.match_cur_tok('L_INL_MATH'):
                # TeX Mode -> Math Mode
                return self.cur_tok

            elif self.match_cur_tok('L_DSP_MATH'):
                # TeX Mode -> Math Mode
                return self.cur_tok

            else:
                print(f"Syntax Error: Unrecognized token {self.cur_tok} \n" 
                      f"{self.tex_lexer.line}  \n"
                      f"{self.tex_lexer.pos*' '}^^^\n")

    def match_next_token(self, token_str) -> bool:
        return self.cur_tok.name == token_str

    def match_cur_tok(self, token_str) -> bool:
        if self.cur_tok.name == token_str:
            return True
        return False

# elif self.match_cur_tok('BACKSLASH'):
#     self.tex_lexer.get_next_token() # Lookahead one token
#     # First we try...
#     # TeX Mode -> Math Mode
#     if self.match_cur_tok('LPAR'): # Classic math
#         self.parse_inline_math(stop_scan='\\)')
#     elif self.match_cur_tok('L_BRACKET'):
#         self.parse_display_math(stop_scan='\\]')
#     # Then we try...
#     # TeX Mode -> Base Language
#     elif (next_tok := self.base_lexer.get_next_token()) == 'FUNCTION':
#         self.add_token('FUNCTION', next_tok.string)
#         self.parse_function_call()  # stop_scan = )
#     elif next_tok == 'LITERAL_CALL':
#         self.add_token('LITERAL_CALL', next_tok.string)
#         self.parse_literal_call()  # stop_scan = }
#     elif next_tok == 'IDENTIFIER':
#         self.add_token('IDENTIFIER', next_tok.string)
#     elif next_tok == 'SPACE':
#         print("Syntax Error: Lonely \\")
#     else:
#         print("Syntax Error following \\")

# TeX Mode -> Base Language
# elif self.match_cur_tok('L_CURLY'):
#     self.parse_program_call()  # stop_scan = }

    # def parse_inline_math(self, *stop_tokens):
    #     while (cur_tok := self.tex_lexer.get_next_token()) != EOF:
    #         if self.match_stop_tokens(cur_tok, stop_tokens):
    #             break
    #         self.parse()
    #     if cur_tok == EOF:
    #         print("Syntax Error: Unbalanced stop tokens for inline math")
    #
    # def parse_display_math(self, *stop_tokens):
    #     while (cur_tok := self.tex_lexer.get_next_token()) != EOF:
    #         if self.match_stop_tokens(cur_tok, stop_tokens):
    #             break
    #         self.parse()
    #     if cur_tok == EOF:
    #         print("Syntax Error: Unbalanced stop tokens for display math")
    #
    # def parse_function_call(self):
    #     while (cur_tok := self.base_lexer.get_next_token()) != EOF:
    #         if cur_tok == 'RPAR':
    #             break
    #         self.base_parser.parse()
    #     if cur_tok == EOF:
    #         print("Syntax Error: Unbalanced )")
    #
    # def parse_literal_call(self):
    #     while (cur_tok := self.tex_lexer.get_next_token()) != EOF:
    #         if cur_tok == 'R_CURLY':
    #             break
    #         self.parse()
    #     if cur_tok == EOF:
    #         print("Syntax Error: Unbalanced }")
    #
    # def parse_program_call(self):
    #     while (cur_tok := self.base_lexer.get_next_token) != EOF:
    #         if cur_tok == 'R_CURLY':
    #             break
    #         self.base_parser.parse()
    #     if cur_tok == EOF:
    #         print("Syntax Error: Unbalanced }")
