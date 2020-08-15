# is_unique with additional data structure
def is_unique_v1(string):
    char_dict = dict()

    for char in string:
        if char not in char_dict:
            char_dict[char] = True
        else:
            return False

    return True


# is_unique without additional data structure
def is_unique_v2(string):
    if len(string) == 1:
        return True

    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True


# is_unique python implementation
def is_unique_pi(string):
    return len(string) == len(set(string))
