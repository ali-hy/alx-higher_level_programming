#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) != dict or len(a_dictionary) == 0:
        return
    keys = list(a_dictionary.keys())
    res = keys[0]
    for key in keys[1:]:
        if a_dictionary[key] > a_dictionary[res]:
            res = key
    return key


if __name__ == '__main__':
    best_score = __import__('10-best_score').best_score

    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))
