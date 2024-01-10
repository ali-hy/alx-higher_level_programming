#!/usr/bin/python3
def only_diff_elements(set_1: set, set_2: set):
    return set_1.difference(set_2).union(set_2.difference(set_1))


if __name__ == '__main__':
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    c_set = only_diff_elements(set_1, set_2)
    print(sorted(list(c_set)))
