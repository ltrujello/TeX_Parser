
def generate_token_code(token_name,
                    value,
                    type,
                    sibling_name,
                    sibling_value):
    token_template = f"""\

def new_{token_name.lower()}_tok():
    {token_name} = Token("{token_name}", "{value}")
    {token_name}.type = "{type}"
    {token_name}.sibling = Token("{sibling_name}", "{sibling_value}")
    return {token_name}

    """
    return token_template


def make_tex_tokens():
    # This can definitely be fancier. Not worth the effort until C.
    token_py_code = []
    with open("tex_tokens.txt", "r") as f:
        lines = f.readlines()
        for line_num in range(len(lines)):
            line_entries = lines[line_num].split()
            if len(line_entries) == 2:
                if len(next_line := lines[line_num + 1].split()) == 3:
                    token_code = generate_token_code(line_entries[0],
                                                     line_entries[1],
                                                     "TeX",
                                                     next_line[1],
                                                     next_line[2])
                else:
                    token_code = generate_token_code(line_entries[0],
                                                     line_entries[1],
                                                     "TeX",
                                                     None,
                                                     None)
                token_py_code.append(token_code)

    # Write the python functions
    with open("tex_tokens.py", "w") as f:
        f.write("# Auto-generated from token_generator.py\n")
        f.write("from frontend_py.token.token import Token\n")
        f.writelines(token_py_code)

def make_math_tokens():
    token_py_code = []
    with open("math_tokens.txt", "r") as f:
        lines = f.readlines()
        for line_num in range(len(lines)):
            line_entries = lines[line_num].split()
            if len(line_entries) == 2:
                if len(next_line := lines[line_num + 1].split()) == 3:
                    token_code = generate_token_code(line_entries[0],
                                                     line_entries[1],
                                                     "Math",
                                                     next_line[1],
                                                     next_line[2])
                else:
                    token_code = generate_token_code(line_entries[0],
                                                     line_entries[1],
                                                     "Math",
                                                     None,
                                                     None)
                token_py_code.append(token_code)

    # Write the python functions
    with open("math_tokens.py", "w") as f:
        f.write("# Auto-generated from token_generator.py\n")
        f.write("from frontend_py.token.token import Token\n")
        f.writelines(token_py_code)
