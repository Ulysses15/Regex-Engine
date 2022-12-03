def single_character_string(a, b) -> "return True if characters match":
    """check if two characters match"""
    if len(a) == 0:
        return True
    elif len(b) == 0:
        return False
    else:
        if a == '.':
            return True
        else:
            if a == b:
                return True
            else:
                return False


def meta_result(temp) -> "check if template includes meta characters":
    meta_chars = ['?', '*', '+']
    if len(temp) >= 2:
        if temp[1] in meta_chars:
            if temp[0] != '\\':
                k_1 = temp.replace(temp[1], '', 1)  # replace meta mark
                return k_1, temp[1]
            else:
                k_2 = temp.replace(temp[0], '', 1)  # replace escape char
                return k_2, 'escape_character'


def check_with_star(x, string) -> "x for no char":
    """the * operator means zero or more characters"""
    if len(x) == 1:
        return True
    if x[0] == '.':
        return check_pair_by_pair_reverse(x, string)
    if single_character_string(x[0], string[0]):
        if check_pair_by_pair(x[1:], string[1:]):
            return True
        if string[0] == string[1]:
            if check_pair_by_pair(x[0], string[1:]):
                return True
        else:
            return False
    if single_character_string(x[1], string[0]):
        if check_pair_by_pair(x[2:], string[1:]):
            return True
        else:
            return False
    else:
        return False


def check_with_question(x, string):
    """the ? operator means zero or one character"""
    if len(x) == 1:
        return True
    if single_character_string(x[0], string[0]):
        if check_pair_by_pair(x[1:], string[1:]):
            return True
        else:
            return False
    if single_character_string(x[1], string[0]):
        if check_pair_by_pair(x[2:], string[1:]):
            return True
        else:
            return False
    else:
        return False


def check_with_plus(x, string) -> "x with '+' replaced":
    """the + operator means one or more characters"""
    if single_character_string(x[0], string[0]):
        if check_pair_by_pair(x[1:], string[1:]):
            return True
        if string[0] == string[1]:
            if check_pair_by_pair(x[0], string[1:]):
                return True
    else:
        return False


def check_pair_by_pair(template, check_string) -> "Strings are of Equal length! " \
                                                  "return True if lines are identical":
    """check if two strings match symbol by symbol.
    template may be less than string, the opposite
    is False"""
    if not template:  # exit from recursion
        return True
    if not check_string:  # exit from recursion
        return False
    if meta_result(template):
        t, meta_flag = meta_result(template)
        if meta_flag == '?':
            return check_with_question(t, check_string)
        if meta_flag == '*':
            return check_with_star(t, check_string)
        if meta_flag == '+':
            return check_with_plus(t, check_string)
        if meta_flag == 'escape_character':
            return check_pair_by_pair(t, check_string)
    if template[0] == '\\':
        if len(template) > 1:
            if template[1] == '.' and check_string[1] == '.':
                return check_pair_by_pair(template[2:], check_string[2:])
            if template[1] == '\\' and check_string[0] == '\\':
                return check_pair_by_pair(template[2:], check_string[1:])
            else:
                return False
        else:
            if check_string[0] == '\\':
                return True
            else:
                return False
    elif single_character_string(template[0], check_string[0]):
        return check_pair_by_pair(template[1:], check_string[1:])
    else:
        return False


def check_pair_by_pair_reverse(template, check_string) -> "Strings are of Equal length! " \
                                                          "(if not with meta)":
    """reverse check"""
    if not template:  # exit from recursion
        return True
    if template[-1] in ['+', '*', '?']:
        return check_pair_by_pair(template, check_string)
    if single_character_string(template[-1], check_string[-1]):
        return check_pair_by_pair_reverse(template[0:-2], check_string[0:-2])
    else:
        return False


def check_different_lines(template_line, string_line) -> "Stage 3 Check lines of different length" \
                                                         "work as findall() func":
    if not string_line:
        return False
    if check_pair_by_pair(template_line, string_line) is False:
        return check_different_lines(template_line, string_line[1::])
    if check_pair_by_pair(template_line, string_line) is True:
        return True


def check_strict_template(template) -> "check if template is strict with ^ and $":
    """check if template is strict with ^ and $"""
    if template:
        if template[0] == '^':
            if template[len(template) - 1] == '$':
                return 'strict'
            else:
                return 'start'
        elif template[len(template) - 1] == '$':
            return 'end'
        else:
            return 'common'


def strict_template(a, b):
    template = a[1:len(a)-1]
    if check_pair_by_pair_reverse(template, b):
        if check_pair_by_pair(template, b):
            return True
        else:
            return False
    else:
        return False


def start_template(x, y):
    template = x[1:]
    return check_pair_by_pair(template, y)


def common_template(g, h):
    return check_different_lines(g, h)


def end_template(m, n):
    template = m[: -1]
    string = n[-len(template):]
    return check_pair_by_pair(template, string)


def meta_start_end(f, g):
    if check_strict_template(f) == 'end':
        return end_template(f, g)
    if check_strict_template(f) == 'common':
        return common_template(f, g)
    if check_strict_template(f) == 'strict':
        return strict_template(f, g)
    if check_strict_template(f) == 'start':
        return start_template(f, g)
    if not check_strict_template(f):
        return True


def main():
    reg, st = input().split('|')
    # reg = "\\"
    # st = '\\'
    print(meta_start_end(reg, st))  # main function


if __name__ == '__main__':
    main()
