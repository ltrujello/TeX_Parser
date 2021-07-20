// Auto-generated from token_generator.py

#include <stdlib.h> 
#include <stdio.h>   
#include <string.h>
#include "tex_tokens.h"  
#include "token.h"



Token new_t_word_token(void){
    Token T_WORD = malloc(sizeof *T_WORD);
    if (T_WORD == NULL){
        printf("Memory allocation for T_WORD token failed");
        return NULL;
    }
    T_WORD->name  = strdup("T_WORD");
    T_WORD->value = strdup("None");
    T_WORD->type  = 1;
    
    return T_WORD;
}


Token new_t_space_token(void){
    Token T_SPACE = malloc(sizeof *T_SPACE);
    if (T_SPACE == NULL){
        printf("Memory allocation for T_SPACE token failed");
        return NULL;
    }
    T_SPACE->name  = strdup("T_SPACE");
    T_SPACE->value = strdup("None");
    T_SPACE->type  = 1;
    
    return T_SPACE;
}


Token new_t_eol_token(void){
    Token T_EOL = malloc(sizeof *T_EOL);
    if (T_EOL == NULL){
        printf("Memory allocation for T_EOL token failed");
        return NULL;
    }
    T_EOL->name  = strdup("T_EOL");
    T_EOL->value = strdup("None");
    T_EOL->type  = 1;
    
    return T_EOL;
}


Token new_t_escape_char_token(void){
    Token T_ESCAPE_CHAR = malloc(sizeof *T_ESCAPE_CHAR);
    if (T_ESCAPE_CHAR == NULL){
        printf("Memory allocation for T_ESCAPE_CHAR token failed");
        return NULL;
    }
    T_ESCAPE_CHAR->name  = strdup("T_ESCAPE_CHAR");
    T_ESCAPE_CHAR->value = strdup("None");
    T_ESCAPE_CHAR->type  = 1;
    
    return T_ESCAPE_CHAR;
}


Token new_t_eof_token(void){
    Token T_EOF = malloc(sizeof *T_EOF);
    if (T_EOF == NULL){
        printf("Memory allocation for T_EOF token failed");
        return NULL;
    }
    T_EOF->name  = strdup("T_EOF");
    T_EOF->value = strdup("None");
    T_EOF->type  = 1;
    
    return T_EOF;
}


Token new_t_lpar_token(void){
    Token T_LPAR = malloc(sizeof *T_LPAR);
    if (T_LPAR == NULL){
        printf("Memory allocation for T_LPAR token failed");
        return NULL;
    }
    T_LPAR->name  = strdup("T_LPAR");
    T_LPAR->value = strdup("(");
    T_LPAR->type  = 1;
    
    return T_LPAR;
}


Token new_t_rpar_token(void){
    Token T_RPAR = malloc(sizeof *T_RPAR);
    if (T_RPAR == NULL){
        printf("Memory allocation for T_RPAR token failed");
        return NULL;
    }
    T_RPAR->name  = strdup("T_RPAR");
    T_RPAR->value = strdup(")");
    T_RPAR->type  = 1;
    
    return T_RPAR;
}


Token new_t_lsqb_token(void){
    Token T_LSQB = malloc(sizeof *T_LSQB);
    if (T_LSQB == NULL){
        printf("Memory allocation for T_LSQB token failed");
        return NULL;
    }
    T_LSQB->name  = strdup("T_LSQB");
    T_LSQB->value = strdup("[");
    T_LSQB->type  = 1;
    
    return T_LSQB;
}


Token new_t_rsqb_token(void){
    Token T_RSQB = malloc(sizeof *T_RSQB);
    if (T_RSQB == NULL){
        printf("Memory allocation for T_RSQB token failed");
        return NULL;
    }
    T_RSQB->name  = strdup("T_RSQB");
    T_RSQB->value = strdup("]");
    T_RSQB->type  = 1;
    
    return T_RSQB;
}


Token new_t_lbrace_token(void){
    Token T_LBRACE = malloc(sizeof *T_LBRACE);
    if (T_LBRACE == NULL){
        printf("Memory allocation for T_LBRACE token failed");
        return NULL;
    }
    T_LBRACE->name  = strdup("T_LBRACE");
    T_LBRACE->value = strdup("{");
    T_LBRACE->type  = 1;
    T_LBRACE->sibling = new_t_rbrace_token();
    return T_LBRACE;
}


Token new_t_rbrace_token(void){
    Token T_RBRACE = malloc(sizeof *T_RBRACE);
    if (T_RBRACE == NULL){
        printf("Memory allocation for T_RBRACE token failed");
        return NULL;
    }
    T_RBRACE->name  = strdup("T_RBRACE");
    T_RBRACE->value = strdup("}");
    T_RBRACE->type  = 1;
    
    return T_RBRACE;
}


Token new_t_newline_token(void){
    Token T_NEWLINE = malloc(sizeof *T_NEWLINE);
    if (T_NEWLINE == NULL){
        printf("Memory allocation for T_NEWLINE token failed");
        return NULL;
    }
    T_NEWLINE->name  = strdup("T_NEWLINE");
    T_NEWLINE->value = strdup("\\\\");
    T_NEWLINE->type  = 1;
    
    return T_NEWLINE;
}


Token new_t_dollar_token(void){
    Token T_DOLLAR = malloc(sizeof *T_DOLLAR);
    if (T_DOLLAR == NULL){
        printf("Memory allocation for T_DOLLAR token failed");
        return NULL;
    }
    T_DOLLAR->name  = strdup("T_DOLLAR");
    T_DOLLAR->value = strdup("$");
    T_DOLLAR->type  = 1;
    
    return T_DOLLAR;
}


Token new_t_dbl_dollar_token(void){
    Token T_DBL_DOLLAR = malloc(sizeof *T_DBL_DOLLAR);
    if (T_DBL_DOLLAR == NULL){
        printf("Memory allocation for T_DBL_DOLLAR token failed");
        return NULL;
    }
    T_DBL_DOLLAR->name  = strdup("T_DBL_DOLLAR");
    T_DBL_DOLLAR->value = strdup("$$");
    T_DBL_DOLLAR->type  = 1;
    
    return T_DBL_DOLLAR;
}


Token new_t_l_inl_math_token(void){
    Token T_L_INL_MATH = malloc(sizeof *T_L_INL_MATH);
    if (T_L_INL_MATH == NULL){
        printf("Memory allocation for T_L_INL_MATH token failed");
        return NULL;
    }
    T_L_INL_MATH->name  = strdup("T_L_INL_MATH");
    T_L_INL_MATH->value = strdup("\\(");
    T_L_INL_MATH->type  = 1;
    
    return T_L_INL_MATH;
}


Token new_t_r_inl_math_token(void){
    Token T_R_INL_MATH = malloc(sizeof *T_R_INL_MATH);
    if (T_R_INL_MATH == NULL){
        printf("Memory allocation for T_R_INL_MATH token failed");
        return NULL;
    }
    T_R_INL_MATH->name  = strdup("T_R_INL_MATH");
    T_R_INL_MATH->value = strdup("\\)");
    T_R_INL_MATH->type  = 1;
    
    return T_R_INL_MATH;
}


Token new_t_l_dsp_math_token(void){
    Token T_L_DSP_MATH = malloc(sizeof *T_L_DSP_MATH);
    if (T_L_DSP_MATH == NULL){
        printf("Memory allocation for T_L_DSP_MATH token failed");
        return NULL;
    }
    T_L_DSP_MATH->name  = strdup("T_L_DSP_MATH");
    T_L_DSP_MATH->value = strdup("\\[");
    T_L_DSP_MATH->type  = 1;
    
    return T_L_DSP_MATH;
}


Token new_t_r_dsp_math_token(void){
    Token T_R_DSP_MATH = malloc(sizeof *T_R_DSP_MATH);
    if (T_R_DSP_MATH == NULL){
        printf("Memory allocation for T_R_DSP_MATH token failed");
        return NULL;
    }
    T_R_DSP_MATH->name  = strdup("T_R_DSP_MATH");
    T_R_DSP_MATH->value = strdup("\\]");
    T_R_DSP_MATH->type  = 1;
    
    return T_R_DSP_MATH;
}


Token new_t_comma_skip_token(void){
    Token T_COMMA_SKIP = malloc(sizeof *T_COMMA_SKIP);
    if (T_COMMA_SKIP == NULL){
        printf("Memory allocation for T_COMMA_SKIP token failed");
        return NULL;
    }
    T_COMMA_SKIP->name  = strdup("T_COMMA_SKIP");
    T_COMMA_SKIP->value = strdup("\\,");
    T_COMMA_SKIP->type  = 1;
    
    return T_COMMA_SKIP;
}


Token new_t_colon_skip_token(void){
    Token T_COLON_SKIP = malloc(sizeof *T_COLON_SKIP);
    if (T_COLON_SKIP == NULL){
        printf("Memory allocation for T_COLON_SKIP token failed");
        return NULL;
    }
    T_COLON_SKIP->name  = strdup("T_COLON_SKIP");
    T_COLON_SKIP->value = strdup("\\:");
    T_COLON_SKIP->type  = 1;
    
    return T_COLON_SKIP;
}


Token new_t_semic_skip_token(void){
    Token T_SEMIC_SKIP = malloc(sizeof *T_SEMIC_SKIP);
    if (T_SEMIC_SKIP == NULL){
        printf("Memory allocation for T_SEMIC_SKIP token failed");
        return NULL;
    }
    T_SEMIC_SKIP->name  = strdup("T_SEMIC_SKIP");
    T_SEMIC_SKIP->value = strdup("\\;");
    T_SEMIC_SKIP->type  = 1;
    
    return T_SEMIC_SKIP;
}


Token new_t_exclm_skip_token(void){
    Token T_EXCLM_SKIP = malloc(sizeof *T_EXCLM_SKIP);
    if (T_EXCLM_SKIP == NULL){
        printf("Memory allocation for T_EXCLM_SKIP token failed");
        return NULL;
    }
    T_EXCLM_SKIP->name  = strdup("T_EXCLM_SKIP");
    T_EXCLM_SKIP->value = strdup("\\!");
    T_EXCLM_SKIP->type  = 1;
    
    return T_EXCLM_SKIP;
}


Token new_t_rcart_skip_token(void){
    Token T_RCART_SKIP = malloc(sizeof *T_RCART_SKIP);
    if (T_RCART_SKIP == NULL){
        printf("Memory allocation for T_RCART_SKIP token failed");
        return NULL;
    }
    T_RCART_SKIP->name  = strdup("T_RCART_SKIP");
    T_RCART_SKIP->value = strdup("\\>");
    T_RCART_SKIP->type  = 1;
    
    return T_RCART_SKIP;
}


Token new_t_nobreak_token(void){
    Token T_NOBREAK = malloc(sizeof *T_NOBREAK);
    if (T_NOBREAK == NULL){
        printf("Memory allocation for T_NOBREAK token failed");
        return NULL;
    }
    T_NOBREAK->name  = strdup("T_NOBREAK");
    T_NOBREAK->value = strdup("~");
    T_NOBREAK->type  = 1;
    
    return T_NOBREAK;
}


Token new_t_l_quote_token(void){
    Token T_L_QUOTE = malloc(sizeof *T_L_QUOTE);
    if (T_L_QUOTE == NULL){
        printf("Memory allocation for T_L_QUOTE token failed");
        return NULL;
    }
    T_L_QUOTE->name  = strdup("T_L_QUOTE");
    T_L_QUOTE->value = strdup("``");
    T_L_QUOTE->type  = 1;
    
    return T_L_QUOTE;
}


Token new_t_r_quote_token(void){
    Token T_R_QUOTE = malloc(sizeof *T_R_QUOTE);
    if (T_R_QUOTE == NULL){
        printf("Memory allocation for T_R_QUOTE token failed");
        return NULL;
    }
    T_R_QUOTE->name  = strdup("T_R_QUOTE");
    T_R_QUOTE->value = strdup("''");
    T_R_QUOTE->type  = 1;
    
    return T_R_QUOTE;
}

