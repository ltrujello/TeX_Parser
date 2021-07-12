#ifndef TEX_COMPILER_TOKEN_H
#define TEX_COMPILER_TOKEN_H

struct token {
    char *name;
    char *value;
    int type;
    struct token *sibling;
};

typedef struct token *Token;

#endif //TEX_COMPILER_TOKEN_H
