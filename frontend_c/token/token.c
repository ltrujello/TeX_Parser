#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "token.h"

Token new_tokname_token(char *name, char *value){
    struct token *tokname = malloc(sizeof *tokname);
    if (tokname == NULL){
        printf("Memory allocation for  token failed");
        return NULL;
    }
    tokname->name = strdup(name);
    tokname->value = strdup(value);
    tokname->type = 0;
    return tokname;
}

