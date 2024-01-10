#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())

    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))


if __name__ == '__main__':
    a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
    print_sorted_dictionary(a_dictionary)
