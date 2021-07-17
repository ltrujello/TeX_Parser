// Auto-generated from token_generator.py
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "token.h"


Token new_m_word_token(void){
    struct token *M_WORD = malloc(sizeof *M_WORD);
    if (M_WORD == NULL){
        printf("Memory allocation for M_WORD token failed");
        return NULL;
    }
    M_WORD->name = "M_WORD";
    M_WORD->value = "";
    M_WORD->type =    1;
    
    return M_WORD;
}

Token new_m_space_token(void){
    struct token *M_SPACE = malloc(sizeof *M_SPACE);
    if (M_SPACE == NULL){
        printf("Memory allocation for M_SPACE token failed");
        return NULL;
    }
    M_SPACE->name = "M_SPACE";
    M_SPACE->value = "";
    M_SPACE->type =    1;
    
    return M_SPACE;
}

Token new_m_comment_token(void){
    struct token *M_COMMENT = malloc(sizeof *M_COMMENT);
    if (M_COMMENT == NULL){
        printf("Memory allocation for M_COMMENT token failed");
        return NULL;
    }
    M_COMMENT->name = "M_COMMENT";
    M_COMMENT->value = "";
    M_COMMENT->type =    1;
    
    return M_COMMENT;
}

Token new_m_eol_token(void){
    struct token *M_EOL = malloc(sizeof *M_EOL);
    if (M_EOL == NULL){
        printf("Memory allocation for M_EOL token failed");
        return NULL;
    }
    M_EOL->name = "M_EOL";
    M_EOL->value = "";
    M_EOL->type =    1;
    
    return M_EOL;
}

Token new_m_escape_char_token(void){
    struct token *M_ESCAPE_CHAR = malloc(sizeof *M_ESCAPE_CHAR);
    if (M_ESCAPE_CHAR == NULL){
        printf("Memory allocation for M_ESCAPE_CHAR token failed");
        return NULL;
    }
    M_ESCAPE_CHAR->name = "M_ESCAPE_CHAR";
    M_ESCAPE_CHAR->value = "";
    M_ESCAPE_CHAR->type =    1;
    
    return M_ESCAPE_CHAR;
}

Token new_m_sub_token(void){
    struct token *M_SUB = malloc(sizeof *M_SUB);
    if (M_SUB == NULL){
        printf("Memory allocation for M_SUB token failed");
        return NULL;
    }
    M_SUB->name = "M_SUB";
    M_SUB->value = "_";
    M_SUB->type =    1;
    
    return M_SUB;
}

Token new_m_sup_token(void){
    struct token *M_SUP = malloc(sizeof *M_SUP);
    if (M_SUP == NULL){
        printf("Memory allocation for M_SUP token failed");
        return NULL;
    }
    M_SUP->name = "M_SUP";
    M_SUP->value = "^";
    M_SUP->type =    1;
    
    return M_SUP;
}

Token new_m_align_token(void){
    struct token *M_ALIGN = malloc(sizeof *M_ALIGN);
    if (M_ALIGN == NULL){
        printf("Memory allocation for M_ALIGN token failed");
        return NULL;
    }
    M_ALIGN->name = "M_ALIGN";
    M_ALIGN->value = "&";
    M_ALIGN->type =    1;
    
    return M_ALIGN;
}

Token new_m_newline_token(void){
    struct token *M_NEWLINE = malloc(sizeof *M_NEWLINE);
    if (M_NEWLINE == NULL){
        printf("Memory allocation for M_NEWLINE token failed");
        return NULL;
    }
    M_NEWLINE->name = "M_NEWLINE";
    M_NEWLINE->value = "\\\\";
    M_NEWLINE->type =    1;
    
    return M_NEWLINE;
}

Token new_m_lpar_token(void){
    struct token *M_LPAR = malloc(sizeof *M_LPAR);
    if (M_LPAR == NULL){
        printf("Memory allocation for M_LPAR token failed");
        return NULL;
    }
    M_LPAR->name = "M_LPAR";
    M_LPAR->value = "(";
    M_LPAR->type =    1;
    
    return M_LPAR;
}

Token new_m_rpar_token(void){
    struct token *M_RPAR = malloc(sizeof *M_RPAR);
    if (M_RPAR == NULL){
        printf("Memory allocation for M_RPAR token failed");
        return NULL;
    }
    M_RPAR->name = "M_RPAR";
    M_RPAR->value = ")";
    M_RPAR->type =    1;
    
    return M_RPAR;
}

Token new_m_lsqb_token(void){
    struct token *M_LSQB = malloc(sizeof *M_LSQB);
    if (M_LSQB == NULL){
        printf("Memory allocation for M_LSQB token failed");
        return NULL;
    }
    M_LSQB->name = "M_LSQB";
    M_LSQB->value = "[";
    M_LSQB->type =    1;
    
    return M_LSQB;
}

Token new_m_rsqb_token(void){
    struct token *M_RSQB = malloc(sizeof *M_RSQB);
    if (M_RSQB == NULL){
        printf("Memory allocation for M_RSQB token failed");
        return NULL;
    }
    M_RSQB->name = "M_RSQB";
    M_RSQB->value = "]";
    M_RSQB->type =    1;
    
    return M_RSQB;
}

Token new_m_rbrace_token(void){
    struct token *M_RBRACE = malloc(sizeof *M_RBRACE);
    if (M_RBRACE == NULL){
        printf("Memory allocation for M_RBRACE token failed");
        return NULL;
    }
    M_RBRACE->name = "M_RBRACE";
    M_RBRACE->value = "}";
    M_RBRACE->type =    1;
    
    return M_RBRACE;
}

Token new_m_lbrace_token(void){
    struct token *M_LBRACE = malloc(sizeof *M_LBRACE);
    if (M_LBRACE == NULL){
        printf("Memory allocation for M_LBRACE token failed");
        return NULL;
    }
    M_LBRACE->name = "M_LBRACE";
    M_LBRACE->value = "{";
    M_LBRACE->type =    1;
    M_LBRACE->sibling = new_m_rbrace_token();
    return M_LBRACE;
}

Token new_m_stop_dollar_token(void){
    struct token *M_STOP_DOLLAR = malloc(sizeof *M_STOP_DOLLAR);
    if (M_STOP_DOLLAR == NULL){
        printf("Memory allocation for M_STOP_DOLLAR token failed");
        return NULL;
    }
    M_STOP_DOLLAR->name = "M_STOP_DOLLAR";
    M_STOP_DOLLAR->value = "$";
    M_STOP_DOLLAR->type =    1;
    
    return M_STOP_DOLLAR;
}

Token new_m_stop_dbl_dollar_token(void){
    struct token *M_STOP_DBL_DOLLAR = malloc(sizeof *M_STOP_DBL_DOLLAR);
    if (M_STOP_DBL_DOLLAR == NULL){
        printf("Memory allocation for M_STOP_DBL_DOLLAR token failed");
        return NULL;
    }
    M_STOP_DBL_DOLLAR->name = "M_STOP_DBL_DOLLAR";
    M_STOP_DBL_DOLLAR->value = "$$";
    M_STOP_DBL_DOLLAR->type =    1;
    
    return M_STOP_DBL_DOLLAR;
}

Token new_m_stop_inl_math_token(void){
    struct token *M_STOP_INL_MATH = malloc(sizeof *M_STOP_INL_MATH);
    if (M_STOP_INL_MATH == NULL){
        printf("Memory allocation for M_STOP_INL_MATH token failed");
        return NULL;
    }
    M_STOP_INL_MATH->name = "M_STOP_INL_MATH";
    M_STOP_INL_MATH->value = "\\)";
    M_STOP_INL_MATH->type =    1;
    
    return M_STOP_INL_MATH;
}

Token new_m_stop_dsp_math_token(void){
    struct token *M_STOP_DSP_MATH = malloc(sizeof *M_STOP_DSP_MATH);
    if (M_STOP_DSP_MATH == NULL){
        printf("Memory allocation for M_STOP_DSP_MATH token failed");
        return NULL;
    }
    M_STOP_DSP_MATH->name = "M_STOP_DSP_MATH";
    M_STOP_DSP_MATH->value = "\\]";
    M_STOP_DSP_MATH->type =    1;
    
    return M_STOP_DSP_MATH;
}

Token new_m_rsub_grp_token(void){
    struct token *M_RSUB_GRP = malloc(sizeof *M_RSUB_GRP);
    if (M_RSUB_GRP == NULL){
        printf("Memory allocation for M_RSUB_GRP token failed");
        return NULL;
    }
    M_RSUB_GRP->name = "M_RSUB_GRP";
    M_RSUB_GRP->value = "}";
    M_RSUB_GRP->type =    1;
    
    return M_RSUB_GRP;
}

Token new_m_lsub_grp_token(void){
    struct token *M_LSUB_GRP = malloc(sizeof *M_LSUB_GRP);
    if (M_LSUB_GRP == NULL){
        printf("Memory allocation for M_LSUB_GRP token failed");
        return NULL;
    }
    M_LSUB_GRP->name = "M_LSUB_GRP";
    M_LSUB_GRP->value = "_{";
    M_LSUB_GRP->type =    1;
    M_LSUB_GRP->sibling = new_m_rsub_grp_token();
    return M_LSUB_GRP;
}

Token new_m_rsup_grp_token(void){
    struct token *M_RSUP_GRP = malloc(sizeof *M_RSUP_GRP);
    if (M_RSUP_GRP == NULL){
        printf("Memory allocation for M_RSUP_GRP token failed");
        return NULL;
    }
    M_RSUP_GRP->name = "M_RSUP_GRP";
    M_RSUP_GRP->value = "}";
    M_RSUP_GRP->type =    1;
    
    return M_RSUP_GRP;
}

Token new_m_lsup_grp_token(void){
    struct token *M_LSUP_GRP = malloc(sizeof *M_LSUP_GRP);
    if (M_LSUP_GRP == NULL){
        printf("Memory allocation for M_LSUP_GRP token failed");
        return NULL;
    }
    M_LSUP_GRP->name = "M_LSUP_GRP";
    M_LSUP_GRP->value = "^{";
    M_LSUP_GRP->type =    1;
    M_LSUP_GRP->sibling = new_m_rsup_grp_token();
    return M_LSUP_GRP;
}

Token new_m_lset_brace_token(void){
    struct token *M_LSET_BRACE = malloc(sizeof *M_LSET_BRACE);
    if (M_LSET_BRACE == NULL){
        printf("Memory allocation for M_LSET_BRACE token failed");
        return NULL;
    }
    M_LSET_BRACE->name = "M_LSET_BRACE";
    M_LSET_BRACE->value = "\\{";
    M_LSET_BRACE->type =    1;
    
    return M_LSET_BRACE;
}

Token new_m_rset_brace_token(void){
    struct token *M_RSET_BRACE = malloc(sizeof *M_RSET_BRACE);
    if (M_RSET_BRACE == NULL){
        printf("Memory allocation for M_RSET_BRACE token failed");
        return NULL;
    }
    M_RSET_BRACE->name = "M_RSET_BRACE";
    M_RSET_BRACE->value = "\\}";
    M_RSET_BRACE->type =    1;
    
    return M_RSET_BRACE;
}