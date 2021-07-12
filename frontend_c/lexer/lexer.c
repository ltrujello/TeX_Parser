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


    // Single character tokens


    // Two character tokens

}


