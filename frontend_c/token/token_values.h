// Auto-generated from token_generator.py
#ifndef TEX_COMPILER_TOKEN_VALUES_H
#define TEX_COMPILER_TOKEN_VALUES_H

const unsigned long hash(const char *str) { 
    // Excellent hash function known as djb2.
    unsigned long hash = 5381;  
    int c;

    while (c = *str++)
        hash = ((hash << 5) + hash) + c;
    return hash;
}

#define LPAR 6384261460 
#define RPAR 6384477082 
#define LSQB 6384265239 
#define RSQB 6384480861 
#define LBRACE 6952444721742 
#define RBRACE 6952679534100 
#define BACKLASH 7570784251229502 
#define DOLLAR 6952146851875 
#define COMMA 210669931922 
#define COLON 210669930912 
#define SEMICOLON 249859972537086990 
#define EXCLM 210672616286 
#define TILDE 210689875575 
#define BACKTICK 7570784251525185 
#define RANGLE 6952678211262 
#define SINGLEQTE 249860144234375601 
#define CARET 210669434004 
#define AMPER 210667491226 
#define UNDERSCORE 8245484186229831423 
#endif //TEX_COMPILER_TOKEN_VALUES_H
