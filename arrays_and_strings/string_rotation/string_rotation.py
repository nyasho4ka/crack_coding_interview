def is_rotation(word, rotation):
    if len(word) != len(rotation):
        return False

    if len(word) <= 1:
        if word != rotation:
            return False
        return True

    for i in range(1, len(rotation)):
        if rotation[:i] in word and rotation[i:] in word:
            return True

    return False
