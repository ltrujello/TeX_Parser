// Auto-generated from token_generator.py
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "token.h"


Token new_word_token(void){
    struct token *WORD = malloc(sizeof *WORD);
    if (WORD == NULL){
        printf("Memory allocation for WORD token failed");
        return NULL;
    }
    WORD->name = "WORD";
    WORD->value = "";
    WORD->type =    1;
    
    return WORD;
}

Token new_space_token(void){
    struct token *SPACE = malloc(sizeof *SPACE);
    if (SPACE == NULL){
        printf("Memory allocation for SPACE token failed");
        return NULL;
    }
    SPACE->name = "SPACE";
    SPACE->value = "";
    SPACE->type =    1;
    
    return SPACE;
}

Token new_comment_token(void){
    struct token *COMMENT = malloc(sizeof *COMMENT);
    if (COMMENT == NULL){
        printf("Memory allocation for COMMENT token failed");
        return NULL;
    }
    COMMENT->name = "COMMENT";
    COMMENT->value = "";
    COMMENT->type =    1;
    
    return COMMENT;
}

Token new_eol_token(void){
    struct token *EOL = malloc(sizeof *EOL);
    if (EOL == NULL){
        printf("Memory allocation for EOL token failed");
        return NULL;
    }
    EOL->name = "EOL";
    EOL->value = "";
    EOL->type =    1;
    
    return EOL;
}

Token new_escape_char_token(void){
    struct token *ESCAPE_CHAR = malloc(sizeof *ESCAPE_CHAR);
    if (ESCAPE_CHAR == NULL){
        printf("Memory allocation for ESCAPE_CHAR token failed");
        return NULL;
    }
    ESCAPE_CHAR->name = "ESCAPE_CHAR";
    ESCAPE_CHAR->value = "";
    ESCAPE_CHAR->type =    1;
    
    return ESCAPE_CHAR;
}

Token new_sub_token(void){
    struct token *SUB = malloc(sizeof *SUB);
    if (SUB == NULL){
        printf("Memory allocation for SUB token failed");
        return NULL;
    }
    SUB->name = "SUB";
    SUB->value = "_";
    SUB->type =    1;
    
    return SUB;
}

Token new_sup_token(void){
    struct token *SUP = malloc(sizeof *SUP);
    if (SUP == NULL){
        printf("Memory allocation for SUP token failed");
        return NULL;
    }
    SUP->name = "SUP";
    SUP->value = "^";
    SUP->type =    1;
    
    return SUP;
}

Token new_align_token(void){
    struct token *ALIGN = malloc(sizeof *ALIGN);
    if (ALIGN == NULL){
        printf("Memory allocation for ALIGN token failed");
        return NULL;
    }
    ALIGN->name = "ALIGN";
    ALIGN->value = "&";
    ALIGN->type =    1;
    
    return ALIGN;
}

Token new_newline_token(void){
    struct token *NEWLINE = malloc(sizeof *NEWLINE);
    if (NEWLINE == NULL){
        printf("Memory allocation for NEWLINE token failed");
        return NULL;
    }
    NEWLINE->name = "NEWLINE";
    NEWLINE->value = "\\\\";
    NEWLINE->type =    1;
    
    return NEWLINE;
}

Token new_lpar_token(void){
    struct token *LPAR = malloc(sizeof *LPAR);
    if (LPAR == NULL){
        printf("Memory allocation for LPAR token failed");
        return NULL;
    }
    LPAR->name = "LPAR";
    LPAR->value = "(";
    LPAR->type =    1;
    
    return LPAR;
}

Token new_rpar_token(void){
    struct token *RPAR = malloc(sizeof *RPAR);
    if (RPAR == NULL){
        printf("Memory allocation for RPAR token failed");
        return NULL;
    }
    RPAR->name = "RPAR";
    RPAR->value = ")";
    RPAR->type =    1;
    
    return RPAR;
}

Token new_lsqb_token(void){
    struct token *LSQB = malloc(sizeof *LSQB);
    if (LSQB == NULL){
        printf("Memory allocation for LSQB token failed");
        return NULL;
    }
    LSQB->name = "LSQB";
    LSQB->value = "[";
    LSQB->type =    1;
    
    return LSQB;
}

Token new_rsqb_token(void){
    struct token *RSQB = malloc(sizeof *RSQB);
    if (RSQB == NULL){
        printf("Memory allocation for RSQB token failed");
        return NULL;
    }
    RSQB->name = "RSQB";
    RSQB->value = "]";
    RSQB->type =    1;
    
    return RSQB;
}

Token new_lbrace_token(void){
    struct token *LBRACE = malloc(sizeof *LBRACE);
    if (LBRACE == NULL){
        printf("Memory allocation for LBRACE token failed");
        return NULL;
    }
    LBRACE->name = "LBRACE";
    LBRACE->value = "{";
    LBRACE->type =    1;
    LBRACE->sibling = new_RBRACE_token)();
    return LBRACE;
}

Token new_backslash_token(void){
    struct token *BACKSLASH = malloc(sizeof *BACKSLASH);
    if (BACKSLASH == NULL){
        printf("Memory allocation for BACKSLASH token failed");
        return NULL;
    }
    BACKSLASH->name = "BACKSLASH";
    BACKSLASH->value = "\\";
    BACKSLASH->type =    1;
    
    return BACKSLASH;
}

Token new_stop_dollar_token(void){
    struct token *STOP_DOLLAR = malloc(sizeof *STOP_DOLLAR);
    if (STOP_DOLLAR == NULL){
        printf("Memory allocation for STOP_DOLLAR token failed");
        return NULL;
    }
    STOP_DOLLAR->name = "STOP_DOLLAR";
    STOP_DOLLAR->value = "$";
    STOP_DOLLAR->type =    1;
    
    return STOP_DOLLAR;
}

Token new_stop_dbl_dollar_token(void){
    struct token *STOP_DBL_DOLLAR = malloc(sizeof *STOP_DBL_DOLLAR);
    if (STOP_DBL_DOLLAR == NULL){
        printf("Memory allocation for STOP_DBL_DOLLAR token failed");
        return NULL;
    }
    STOP_DBL_DOLLAR->name = "STOP_DBL_DOLLAR";
    STOP_DBL_DOLLAR->value = "$$";
    STOP_DBL_DOLLAR->type =    1;
    
    return STOP_DBL_DOLLAR;
}

Token new_stop_inl_math_token(void){
    struct token *STOP_INL_MATH = malloc(sizeof *STOP_INL_MATH);
    if (STOP_INL_MATH == NULL){
        printf("Memory allocation for STOP_INL_MATH token failed");
        return NULL;
    }
    STOP_INL_MATH->name = "STOP_INL_MATH";
    STOP_INL_MATH->value = "\\)";
    STOP_INL_MATH->type =    1;
    
    return STOP_INL_MATH;
}

Token new_stop_dsp_math_token(void){
    struct token *STOP_DSP_MATH = malloc(sizeof *STOP_DSP_MATH);
    if (STOP_DSP_MATH == NULL){
        printf("Memory allocation for STOP_DSP_MATH token failed");
        return NULL;
    }
    STOP_DSP_MATH->name = "STOP_DSP_MATH";
    STOP_DSP_MATH->value = "\\]";
    STOP_DSP_MATH->type =    1;
    
    return STOP_DSP_MATH;
}

Token new_lsub_grp_token(void){
    struct token *LSUB_GRP = malloc(sizeof *LSUB_GRP);
    if (LSUB_GRP == NULL){
        printf("Memory allocation for LSUB_GRP token failed");
        return NULL;
    }
    LSUB_GRP->name = "LSUB_GRP";
    LSUB_GRP->value = "_{";
    LSUB_GRP->type =    1;
    LSUB_GRP->sibling = new_RSUB_GRP_token)();
    return LSUB_GRP;
}

Token new_lsup_grp_token(void){
    struct token *LSUP_GRP = malloc(sizeof *LSUP_GRP);
    if (LSUP_GRP == NULL){
        printf("Memory allocation for LSUP_GRP token failed");
        return NULL;
    }
    LSUP_GRP->name = "LSUP_GRP";
    LSUP_GRP->value = "^{";
    LSUP_GRP->type =    1;
    LSUP_GRP->sibling = new_RSUP_GRP_token)();
    return LSUP_GRP;
}

Token new_lset_brace_token(void){
    struct token *LSET_BRACE = malloc(sizeof *LSET_BRACE);
    if (LSET_BRACE == NULL){
        printf("Memory allocation for LSET_BRACE token failed");
        return NULL;
    }
    LSET_BRACE->name = "LSET_BRACE";
    LSET_BRACE->value = "\\{";
    LSET_BRACE->type =    1;
    
    return LSET_BRACE;
}

Token new_rset_brace_token(void){
    struct token *RSET_BRACE = malloc(sizeof *RSET_BRACE);
    if (RSET_BRACE == NULL){
        printf("Memory allocation for RSET_BRACE token failed");
        return NULL;
    }
    RSET_BRACE->name = "RSET_BRACE";
    RSET_BRACE->value = "\\}";
    RSET_BRACE->type =    1;
    
    return RSET_BRACE;
}