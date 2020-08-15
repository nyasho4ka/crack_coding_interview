def oneaway(original, edited):
    # Если строки равны, то всё чётко
    if original == edited:
        return True

    # Если строки по длине отличаются больше чем на 1, то ложь
    if abs(len(original) - len(edited)) > 1:
        return False

    away_number = 0  # количество опечаток

    """
    Сначала проверим на вставку/удаление.
    На самом деле можно всё рассматривать как вставку,
    Важно только проверять по длине меньшей строки
    """

    # Два разных счётчика для разных слов
    i = 0
    j = 0
    while i < len(original) and j < len(edited):
        # Если буквы не равны
        if original[i] != edited[j]:
            # Увеличиваем количество опечаток на единицу
            away_number += 1
            # Если количество опечаток больше 1, то возвращаем False
            if away_number > 1:
                return False
            # Если длина оригинала меньше, чем редактированной строки
            if len(original) < len(edited):
                # Увеличиваем счётчик длинного слова
                j += 1
                # Идём на следующую итерацию и проверяем ту же букву оригинала
                # И следующую букву редактированного слова
                continue
            # Если длина оригинала больше, чем редактированной строки
            elif len(original) > len(edited):
                # Идём на следующую итерацию и проверяем ту же букву редактированного
                # слова и следующую букву оригинала
                i += 1
                continue

        i += 1
        j += 1

    return True


def get_min_max_word(original, edited):
    if len(original) < len(edited):
        return original, edited
    return edited, original
