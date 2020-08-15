def urlify(string, length):
    char_list = list(string)
    space_number = 0
    # Будем проходить массив символов с конца
    for i in range(length-1, -1, -1):
        # Если очередной символ это пробел
        if string[i] == ' ':
            # Увеличиваем количество пробелов в строке на 1, чтобы двигать дальше
            space_number += 1
            move_list(char_list, length, i, space_number)
            insert_percent_20(char_list, i)
            # Вставляем %20
    return char_list


def move_list(char_list, length, current, space_number):
    from_ = length - 1 + (space_number - 1) * 2
    for j in range(from_, current, -1):
        char_list[j + 2] = char_list[j]


def insert_percent_20(char_list, current):
    char_list[current] = '%'
    char_list[current+1] = '2'
    char_list[current+2] = '0'


def urlify_pi(string, length):
    return list(string[:length].replace(' ', '%20'))
