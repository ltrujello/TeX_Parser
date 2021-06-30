# Auto-generated from token_generator.py
from frontend_py.token.token import Token

def new_lpar_tok():
    LPAR = Token("LPAR", "(")
    LPAR.type = "TeX"
    LPAR.sibling = Token("None", "None")
    return LPAR

    
def new_rpar_tok():
    RPAR = Token("RPAR", ")")
    RPAR.type = "TeX"
    RPAR.sibling = Token("None", "None")
    return RPAR

    
def new_lsqb_tok():
    LSQB = Token("LSQB", "[")
    LSQB.type = "TeX"
    LSQB.sibling = Token("None", "None")
    return LSQB

    
def new_rsqb_tok():
    RSQB = Token("RSQB", "]")
    RSQB.type = "TeX"
    RSQB.sibling = Token("None", "None")
    return RSQB

    
def new_lbrace_tok():
    LBRACE = Token("LBRACE", "{")
    LBRACE.type = "TeX"
    LBRACE.sibling = Token("RBRACE", "}")
    return LBRACE

    
def new_backslash_tok():
    BACKSLASH = Token("BACKSLASH", "\\")
    BACKSLASH.type = "TeX"
    BACKSLASH.sibling = Token("None", "None")
    return BACKSLASH

    
def new_newline_tok():
    NEWLINE = Token("NEWLINE", "\\\\")
    NEWLINE.type = "TeX"
    NEWLINE.sibling = Token("None", "None")
    return NEWLINE

    
def new_dollar_tok():
    DOLLAR = Token("DOLLAR", "$")
    DOLLAR.type = "TeX"
    DOLLAR.sibling = Token("None", "None")
    return DOLLAR

    
def new_dbl_dollar_tok():
    DBL_DOLLAR = Token("DBL_DOLLAR", "$$")
    DBL_DOLLAR.type = "TeX"
    DBL_DOLLAR.sibling = Token("None", "None")
    return DBL_DOLLAR

    
def new_l_inl_math_tok():
    L_INL_MATH = Token("L_INL_MATH", "\\(")
    L_INL_MATH.type = "TeX"
    L_INL_MATH.sibling = Token("None", "None")
    return L_INL_MATH

    
def new_r_inl_math_tok():
    R_INL_MATH = Token("R_INL_MATH", "\\)")
    R_INL_MATH.type = "TeX"
    R_INL_MATH.sibling = Token("None", "None")
    return R_INL_MATH

    
def new_l_dsp_math_tok():
    L_DSP_MATH = Token("L_DSP_MATH", "\\[")
    L_DSP_MATH.type = "TeX"
    L_DSP_MATH.sibling = Token("None", "None")
    return L_DSP_MATH

    
def new_r_dsp_math_tok():
    R_DSP_MATH = Token("R_DSP_MATH", "\\]")
    R_DSP_MATH.type = "TeX"
    R_DSP_MATH.sibling = Token("None", "None")
    return R_DSP_MATH

    
def new_comma_skip_tok():
    COMMA_SKIP = Token("COMMA_SKIP", "\\,")
    COMMA_SKIP.type = "TeX"
    COMMA_SKIP.sibling = Token("None", "None")
    return COMMA_SKIP

    
def new_colon_skip_tok():
    COLON_SKIP = Token("COLON_SKIP", "\\:")
    COLON_SKIP.type = "TeX"
    COLON_SKIP.sibling = Token("None", "None")
    return COLON_SKIP

    
def new_semic_skip_tok():
    SEMIC_SKIP = Token("SEMIC_SKIP", "\\;")
    SEMIC_SKIP.type = "TeX"
    SEMIC_SKIP.sibling = Token("None", "None")
    return SEMIC_SKIP

    
def new_exclm_skip_tok():
    EXCLM_SKIP = Token("EXCLM_SKIP", "\\!")
    EXCLM_SKIP.type = "TeX"
    EXCLM_SKIP.sibling = Token("None", "None")
    return EXCLM_SKIP

    
def new_rcart_skip_tok():
    RCART_SKIP = Token("RCART_SKIP", "\\>")
    RCART_SKIP.type = "TeX"
    RCART_SKIP.sibling = Token("None", "None")
    return RCART_SKIP

    
def new_nobreak_tok():
    NOBREAK = Token("NOBREAK", "~")
    NOBREAK.type = "TeX"
    NOBREAK.sibling = Token("None", "None")
    return NOBREAK

    
def new_l_quote_tok():
    L_QUOTE = Token("L_QUOTE", "``")
    L_QUOTE.type = "TeX"
    L_QUOTE.sibling = Token("None", "None")
    return L_QUOTE

    
def new_r_quote_tok():
    R_QUOTE = Token("R_QUOTE", "''")
    R_QUOTE.type = "TeX"
    R_QUOTE.sibling = Token("None", "None")
    return R_QUOTE

    