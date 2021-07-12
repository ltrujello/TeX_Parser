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
    WORD->type =    0;
    
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
    SPACE->type =    0;
    
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
    COMMENT->type =    0;
    
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
    EOL->type =    0;
    
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
    ESCAPE_CHAR->type =    0;
    
    return ESCAPE_CHAR;
}

Token new_eof_token(void){
    struct token *EOF = malloc(sizeof *EOF);
    if (EOF == NULL){
        printf("Memory allocation for EOF token failed");
        return NULL;
    }
    EOF->name = "EOF";
    EOF->value = "";
    EOF->type =    0;
    
    return EOF;
}

Token new_lpar_token(void){
    struct token *LPAR = malloc(sizeof *LPAR);
    if (LPAR == NULL){
        printf("Memory allocation for LPAR token failed");
        return NULL;
    }
    LPAR->name = "LPAR";
    LPAR->value = "(";
    LPAR->type =    0;
    
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
    RPAR->type =    0;
    
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
    LSQB->type =    0;
    
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
    RSQB->type =    0;
    
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
    LBRACE->type =    0;
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
    BACKSLASH->type =    0;
    
    return BACKSLASH;
}

Token new_newline_token(void){
    struct token *NEWLINE = malloc(sizeof *NEWLINE);
    if (NEWLINE == NULL){
        printf("Memory allocation for NEWLINE token failed");
        return NULL;
    }
    NEWLINE->name = "NEWLINE";
    NEWLINE->value = "\\\\";
    NEWLINE->type =    0;
    
    return NEWLINE;
}

Token new_dollar_token(void){
    struct token *DOLLAR = malloc(sizeof *DOLLAR);
    if (DOLLAR == NULL){
        printf("Memory allocation for DOLLAR token failed");
        return NULL;
    }
    DOLLAR->name = "DOLLAR";
    DOLLAR->value = "$";
    DOLLAR->type =    0;
    
    return DOLLAR;
}

Token new_dbl_dollar_token(void){
    struct token *DBL_DOLLAR = malloc(sizeof *DBL_DOLLAR);
    if (DBL_DOLLAR == NULL){
        printf("Memory allocation for DBL_DOLLAR token failed");
        return NULL;
    }
    DBL_DOLLAR->name = "DBL_DOLLAR";
    DBL_DOLLAR->value = "$$";
    DBL_DOLLAR->type =    0;
    
    return DBL_DOLLAR;
}

Token new_l_inl_math_token(void){
    struct token *L_INL_MATH = malloc(sizeof *L_INL_MATH);
    if (L_INL_MATH == NULL){
        printf("Memory allocation for L_INL_MATH token failed");
        return NULL;
    }
    L_INL_MATH->name = "L_INL_MATH";
    L_INL_MATH->value = "\\(";
    L_INL_MATH->type =    0;
    
    return L_INL_MATH;
}

Token new_r_inl_math_token(void){
    struct token *R_INL_MATH = malloc(sizeof *R_INL_MATH);
    if (R_INL_MATH == NULL){
        printf("Memory allocation for R_INL_MATH token failed");
        return NULL;
    }
    R_INL_MATH->name = "R_INL_MATH";
    R_INL_MATH->value = "\\)";
    R_INL_MATH->type =    0;
    
    return R_INL_MATH;
}

Token new_l_dsp_math_token(void){
    struct token *L_DSP_MATH = malloc(sizeof *L_DSP_MATH);
    if (L_DSP_MATH == NULL){
        printf("Memory allocation for L_DSP_MATH token failed");
        return NULL;
    }
    L_DSP_MATH->name = "L_DSP_MATH";
    L_DSP_MATH->value = "\\[";
    L_DSP_MATH->type =    0;
    
    return L_DSP_MATH;
}

Token new_r_dsp_math_token(void){
    struct token *R_DSP_MATH = malloc(sizeof *R_DSP_MATH);
    if (R_DSP_MATH == NULL){
        printf("Memory allocation for R_DSP_MATH token failed");
        return NULL;
    }
    R_DSP_MATH->name = "R_DSP_MATH";
    R_DSP_MATH->value = "\\]";
    R_DSP_MATH->type =    0;
    
    return R_DSP_MATH;
}

Token new_comma_skip_token(void){
    struct token *COMMA_SKIP = malloc(sizeof *COMMA_SKIP);
    if (COMMA_SKIP == NULL){
        printf("Memory allocation for COMMA_SKIP token failed");
        return NULL;
    }
    COMMA_SKIP->name = "COMMA_SKIP";
    COMMA_SKIP->value = "\\,";
    COMMA_SKIP->type =    0;
    
    return COMMA_SKIP;
}

Token new_colon_skip_token(void){
    struct token *COLON_SKIP = malloc(sizeof *COLON_SKIP);
    if (COLON_SKIP == NULL){
        printf("Memory allocation for COLON_SKIP token failed");
        return NULL;
    }
    COLON_SKIP->name = "COLON_SKIP";
    COLON_SKIP->value = "\\:";
    COLON_SKIP->type =    0;
    
    return COLON_SKIP;
}

Token new_semic_skip_token(void){
    struct token *SEMIC_SKIP = malloc(sizeof *SEMIC_SKIP);
    if (SEMIC_SKIP == NULL){
        printf("Memory allocation for SEMIC_SKIP token failed");
        return NULL;
    }
    SEMIC_SKIP->name = "SEMIC_SKIP";
    SEMIC_SKIP->value = "\\;";
    SEMIC_SKIP->type =    0;
    
    return SEMIC_SKIP;
}

Token new_exclm_skip_token(void){
    struct token *EXCLM_SKIP = malloc(sizeof *EXCLM_SKIP);
    if (EXCLM_SKIP == NULL){
        printf("Memory allocation for EXCLM_SKIP token failed");
        return NULL;
    }
    EXCLM_SKIP->name = "EXCLM_SKIP";
    EXCLM_SKIP->value = "\\!";
    EXCLM_SKIP->type =    0;
    
    return EXCLM_SKIP;
}

Token new_rcart_skip_token(void){
    struct token *RCART_SKIP = malloc(sizeof *RCART_SKIP);
    if (RCART_SKIP == NULL){
        printf("Memory allocation for RCART_SKIP token failed");
        return NULL;
    }
    RCART_SKIP->name = "RCART_SKIP";
    RCART_SKIP->value = "\\>";
    RCART_SKIP->type =    0;
    
    return RCART_SKIP;
}

Token new_nobreak_token(void){
    struct token *NOBREAK = malloc(sizeof *NOBREAK);
    if (NOBREAK == NULL){
        printf("Memory allocation for NOBREAK token failed");
        return NULL;
    }
    NOBREAK->name = "NOBREAK";
    NOBREAK->value = "~";
    NOBREAK->type =    0;
    
    return NOBREAK;
}

Token new_l_quote_token(void){
    struct token *L_QUOTE = malloc(sizeof *L_QUOTE);
    if (L_QUOTE == NULL){
        printf("Memory allocation for L_QUOTE token failed");
        return NULL;
    }
    L_QUOTE->name = "L_QUOTE";
    L_QUOTE->value = "``";
    L_QUOTE->type =    0;
    
    return L_QUOTE;
}

Token new_r_quote_token(void){
    struct token *R_QUOTE = malloc(sizeof *R_QUOTE);
    if (R_QUOTE == NULL){
        printf("Memory allocation for R_QUOTE token failed");
        return NULL;
    }
    R_QUOTE->name = "R_QUOTE";
    R_QUOTE->value = "''";
    R_QUOTE->type =    0;
    
    return R_QUOTE;
}