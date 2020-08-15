import collections


def check_permutation(string_1, string_2):
    if len(string_1) != len(string_2):
        return False

    char_dict = dict()
    # count chars in string 1
    for char in string_1:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    # subtract chars from dict
    for char in string_2:
        if char in char_dict:
            char_dict[char] -= 1
        else:
            return False

    # Now let's check that there's no
    # any value with more than 0 value
    return not sum(char_dict.values())  # if sum > 0 than False


def check_permutation_pi(string_1, string_2):
    # Using more memory
    counter_1 = collections.Counter(string_1)
    counter_2 = collections.Counter(string_2)
    return counter_1 == counter_2
