// Auto-generated by lexer_generator.py
#include <stdio.h>
#include <token.h>
#include <math_tokens.h>
#include <tex_tokens.h>

char *line;
int pos;

Token get_next_token(void){
    cur_char = line[pos];

    if (is_blank(cur_char))
        return skip_blanks()

    if (isalpha(cur_char))
        return get_word()

    // Backslash tokens
    if (char == "\\")
        switch (next_char = self.line[self.pos]){
            case "\\":
                return new_newline_token();
            case ")":
                return new_stop_inl_math_token();
            case "]":
                return new_stop_dsp_math_token();
            case "{":
                return new_lset_brace_token();
            case "}":
                return new_rset_brace_token();
      }
    // Two character tokens
    if (cur_char == "$"){
        next_char = line[pos + 1];
        if (next_char == "$")
            return new_stop_dbl_dollar_token();
    }
    if (cur_char == "_"){
        next_char = line[pos + 1];
        if (next_char == "{")
            return new_lsub_grp_token();
    }
    if (cur_char == "^"){
        next_char = line[pos + 1];
        if (next_char == "{")
            return new_lsup_grp_token();
    }

    // Single character tokens
    if (cur_char == "_")
        return new_sub_token();
    if (cur_char == "^")
        return new_sup_token();
    if (cur_char == "&")
        return new_align_token();
    if (cur_char == "(")
        return new_lpar_token();
    if (cur_char == ")")
        return new_rpar_token();
    if (cur_char == "[")
        return new_lsqb_token();
    if (cur_char == "]")
        return new_rsqb_token();
    if (cur_char == "{")
        return new_lbrace_token();
    if (cur_char == "}")
        return new_rbrace_token();
    if (cur_char == "\")
        return new_backslash_token();
    if (cur_char == "$")
        return new_stop_dollar_token();
    if (cur_char == "}")
        return new_rsub_grp_token();
    if (cur_char == "}")
        return new_rsup_grp_token();


}



