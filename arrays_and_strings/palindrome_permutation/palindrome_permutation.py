import collections


def palindrome_permutation(string):
    """
    Палиндром это строка, которая одинаково читается справа налево
    и слева направо, а также где каждой буквы чётное количество
    если всего букв чётное количество: арра, лоол абба и прочее
    либо каждой буквы чётное количество, кроме средней буквы
    довод, казак, заказ и т. д.

    То есть нам нужно проверить количество букв в слове.
    Если буква всего одна или ноль, то строка является палиндромом
    Затем считаем количество букв в слове, если нечетных букв > 1
    То не является перестановкой, иначе является
    """
    if len(string) <= 1:
        return True

    string = string.lower()
    odd_number = 0

    for i in range(len(string)):
        char_number = 0
        if string[i] == ' ':
            continue
        for j in range(len(string)):
            if string[i] == string[j]:
                char_number += 1
        if char_number % 2 == 1:
            odd_number += 1
        if odd_number > 1:
            return False

    return True


def palindrome_permutation_pi(string):
    string = string.replace(' ', '').lower()
    counter = collections.Counter(string)
    return not sum([value % 2 for value in counter.values()]) > 1
