def string_compression(string):
    if len(string) <= 1:
        return string

    result_string = ''
    # Переменная, которая хранит возможно повторяющийся символ
    # По умолчанию первый символ
    temp = string[0]
    # Переменная, которая хранит количество повторяющихся символов
    counter = 1
    for i, char in enumerate(string[1:]):
        # Если символ равен символу в буфере
        if char == temp:
            counter += 1
        # Иначе
        else:
            # Выводим символ из temp и counter в строку
            result_string += temp + str(counter)
            # Наткнулись на другой символ, сразу ставим его в temp
            # И присваиваем единицу
            temp = char
            counter = 1

    """
    Так как последняя буква в строке никогда не встретится с
    условием из else ветки, то есть char != temp, значит, что
    цикл пройдет последним if условием и так и не выведет в строку
    последний символ и его количество в строке, но эта информация
    всё равно будет храниться в переменные temp и counter, когда
    мы выйдем из цикла, а значит можно будет просто дописать в конец
    строки эти значения
    """
    result_string += temp + str(counter)

    if len(result_string) >= len(string):
        return string
    return result_string
