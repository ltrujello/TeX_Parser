from frontend_py.lexer.math_lexer import Math_Lexer

#   Possible syntax transitions
#   Tex Mode      -> Base Language
#                 -> Math mode
#
#   Base Language -> Tex Mode
#
#   Math Mode     -> Tex Mode
#                 -> Base Language

class Math_Parser:
    def __init__(self):
        self.math_lexer = Math_Lexer()
        self.tokens = []

    def parse(self, line, pos, stop_scan):
        self.math_lexer.line = line
        self.math_lexer.pos = pos
        while (cur_tok := self.math_lexer.get_next_token()).type != stop_scan.type:
            self.cur_tok = cur_tok
            print(self.cur_tok)

            if self.match_cur_tok('EOF'):
                return self.cur_tok

            # A space token
            if self.match_cur_tok('SPACE'):
                continue

            # A word token
            elif self.match_cur_tok('WORD'):
                continue

            # Program access
            elif self.match_cur_tok('LBRACE'):
                # Math Mode -> Base Language
                return self.cur_tok

            # A new line
            elif self.match_cur_tok('NEWLINE'):
                continue

            # A subscript
            elif self.match_cur_tok('SUB'):
                continue

            # A superscript
            elif self.match_cur_tok('SUP'):
                continue

            # An alignment
            elif self.match_cur_tok('ALIGN'):
                continue

            # A left parenthesis
            elif self.match_cur_tok('LPAR'):
                continue

            # A right parenthesis
            elif self.match_cur_tok('RPAR'):
                continue

            else:
                print(f"Syntax Error: Unrecognized token {self.cur_tok} \n" 
                      f"{self.math_lexer.line}  \n"
                      f"{self.math_lexer.pos*' '}^^^\n")

    def match_next_token(self, token_str) -> bool:
        return self.cur_tok.type == token_str

    def match_cur_tok(self, token_str) -> bool:
        if self.cur_tok.type == token_str:
            self.add_token(self.cur_tok, self.cur_tok.type)
            return True
        return False

    def add_token(self, token, string):
        self.tokens.append((token, string))
