modes = {
    "tex": 0,
    "math": 1,
    "base": 2
}


def make_token_funcs(mode: str) -> None:
    token_fp = f"../../grammar/{mode}_tokens.txt"
    token_c_code = []
    token_h_code = []
    token_c_fp = f"{mode}_tokens.c"
    token_h_fp = f"{mode}_tokens.h"

    with open(token_fp, "r") as f:
        lines = f.readlines()
    line_num = 0
    while line_num < len(lines) - 1:  # We check two lines at a time.
        line_entries = lines[line_num].split()
        token_name = None
        value = ""
        sibling_name = None
        if len(line_entries) == 0:  # Skip a blank line
            line_num += 1
            continue
        if len(line_entries) == 1:  # A Token, with no value
            token_name = line_entries[0]
        elif len(line_entries) == 2:  # A Token and a value
            token_name = line_entries[0]
            value = line_entries[1]
        else:
            num_line_entries(lines[line_num], line_num)
            break
        # Look at the next line
        if len(next_line_entries := lines[line_num + 1].split()) == 3:  # Occurs when we specified a sibling
            if next_line_entries[0] == 'sibling:':
                sibling_name = next_line_entries[1]
                line_num += 1
            else:
                sibling_line_error(lines[line_num], line_num)
                break
        c_code, h_code = generate_token_code(token_name,  # Append token C code
                                                 value,
                                                 modes[mode],
                                                 sibling_name)
        token_c_code.append(c_code)
        token_h_code.append(h_code+";\n")
        line_num += 1

    # Write .c and .h files
    with open(token_c_fp, "w") as f:
        f.write("// Auto-generated from token_generator.py\n")
        f.write("#include <stdlib.h>\n")
        f.write("#include <stdio.h>\n")
        f.write("#include <string.h>\n")
        f.write("#include \"token.h\"\n")
        f.writelines(token_c_code)

    with open(token_h_fp, "w") as f:
        f.write("// Auto-generated from token_generator.py\n")
        f.write("#include \"token.h\"\n\n")
        f.writelines(token_h_code)


def generate_token_code(token_name,
                        value,
                        type,
                        sibling_name):
    declaration = f"Token new_{token_name.lower()}_token(void)"
    if sibling_name is not None:
        sibling_line = f"{token_name}->sibling = new_{sibling_name}_token)();"
    else:
        sibling_line = ""
    token_template = f"""\n
{declaration}{{
    struct token *{token_name} = malloc(sizeof *{token_name});
    if ({token_name} == NULL){{
        printf("Memory allocation for {token_name} token failed");
        return NULL;
    }}
    {token_name}->name = "{token_name}";
    {token_name}->value = "{value}";
    {token_name}->type =    {type};
    {sibling_line}
    return {token_name};
}}"""
    return token_template, declaration


def make_tex_tokens():
    make_token_funcs("tex")


def make_math_tokens():
    make_token_funcs("math")


def sibling_line_error(line, line_num):
    print(f"First entry in line {line_num} is not 'sibling'")
    print(line)


def num_line_entries(line, line_num):
    print(f"Too many entries in line {line_num + 1}:")
    print(line)
