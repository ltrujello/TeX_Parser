from frontend_py.lexer.base_lexer import Base_Lexer

#   Possible syntax transitions
#   Tex Mode      -> Base Language
#                 -> Math mode
#
#   Base Language -> Tex Mode
#
#   Math Mode     -> Tex Mode
#                 -> Base Language


class Base_Parser:
    def __init__(self):
        self.base_lexer = Base_Lexer()
        self.tokens = []

    def parse(self, line, pos, stop_scan=""):
        self.base_lexer.line = line
        self.base_lexer.pos = pos
        while (cur_tok := self.base_lexer.get_next_token()).type != stop_scan:
            self.cur_tok = cur_tok
            print(self.cur_tok)
            if self.match_cur_tok('BASE_PROGRAM'):
                continue
            elif self.match_cur_tok('EOF'):
                return self.cur_tok
            else:
                print(f"Unrecognized token {self.cur_tok}")

    def match_next_token(self, token_str) -> bool:
        return self.cur_tok.type == token_str

    def match_cur_tok(self, token_str) -> bool:
        if self.cur_tok.type == token_str:
            self.add_token(self.cur_tok, self.cur_tok.type)
            return True
        return False

    def add_token(self, token, string):
        self.tokens.append((token, string))
