# Auto-generated from token_generator.py
from frontend_py.token.token import Token

def new_sub_tok():
    SUB = Token("SUB", "_")
    SUB.type = "Math"
    SUB.sibling = Token("None", "None")
    return SUB

    
def new_sup_tok():
    SUP = Token("SUP", "^")
    SUP.type = "Math"
    SUP.sibling = Token("None", "None")
    return SUP

    
def new_align_tok():
    ALIGN = Token("ALIGN", "&")
    ALIGN.type = "Math"
    ALIGN.sibling = Token("None", "None")
    return ALIGN

    
def new_newline_tok():
    NEWLINE = Token("NEWLINE", "\\\\")
    NEWLINE.type = "Math"
    NEWLINE.sibling = Token("None", "None")
    return NEWLINE

    
def new_lpar_tok():
    LPAR = Token("LPAR", "(")
    LPAR.type = "Math"
    LPAR.sibling = Token("None", "None")
    return LPAR

    
def new_rpar_tok():
    RPAR = Token("RPAR", ")")
    RPAR.type = "Math"
    RPAR.sibling = Token("None", "None")
    return RPAR

    
def new_lsqb_tok():
    LSQB = Token("LSQB", "[")
    LSQB.type = "Math"
    LSQB.sibling = Token("None", "None")
    return LSQB

    
def new_rsqb_tok():
    RSQB = Token("RSQB", "]")
    RSQB.type = "Math"
    RSQB.sibling = Token("None", "None")
    return RSQB

    
def new_lbrace_tok():
    LBRACE = Token("LBRACE", "{")
    LBRACE.type = "Math"
    LBRACE.sibling = Token("RBRACE", "}")
    return LBRACE

    
def new_backslash_tok():
    BACKSLASH = Token("BACKSLASH", "\\")
    BACKSLASH.type = "Math"
    BACKSLASH.sibling = Token("None", "None")
    return BACKSLASH

    
def new_stop_dollar_tok():
    STOP_DOLLAR = Token("STOP_DOLLAR", "$")
    STOP_DOLLAR.type = "Math"
    STOP_DOLLAR.sibling = Token("None", "None")
    return STOP_DOLLAR

    
def new_stop_dbl_dollar_tok():
    STOP_DBL_DOLLAR = Token("STOP_DBL_DOLLAR", "$$")
    STOP_DBL_DOLLAR.type = "Math"
    STOP_DBL_DOLLAR.sibling = Token("None", "None")
    return STOP_DBL_DOLLAR

    
def new_stop_inl_math_tok():
    STOP_INL_MATH = Token("STOP_INL_MATH", "\\)")
    STOP_INL_MATH.type = "Math"
    STOP_INL_MATH.sibling = Token("None", "None")
    return STOP_INL_MATH

    
def new_stop_dsp_math_tok():
    STOP_DSP_MATH = Token("STOP_DSP_MATH", "\\]")
    STOP_DSP_MATH.type = "Math"
    STOP_DSP_MATH.sibling = Token("None", "None")
    return STOP_DSP_MATH

    
def new_lsub_grp_tok():
    LSUB_GRP = Token("LSUB_GRP", "_{")
    LSUB_GRP.type = "Math"
    LSUB_GRP.sibling = Token("RSUB_GRP", "}")
    return LSUB_GRP

    
def new_lsup_grp_tok():
    LSUP_GRP = Token("LSUP_GRP", "^{")
    LSUP_GRP.type = "Math"
    LSUP_GRP.sibling = Token("RSUP_GRP", "}")
    return LSUP_GRP

    
def new_lset_brace_tok():
    LSET_BRACE = Token("LSET_BRACE", "\\{")
    LSET_BRACE.type = "Math"
    LSET_BRACE.sibling = Token("None", "None")
    return LSET_BRACE

    
def new_rset_brace_tok():
    RSET_BRACE = Token("RSET_BRACE", "\\}")
    RSET_BRACE.type = "Math"
    RSET_BRACE.sibling = Token("None", "None")
    return RSET_BRACE

    