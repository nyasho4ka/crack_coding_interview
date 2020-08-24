off_limits_table = (
    (1, 3),
    (2, 3),
)

path_list = list()
path_memo = dict()


def path(r, c):
    print('{}, {}, {}'.format(r, c, (r, c) in off_limits_table))
    if tuple((r, c)) in off_limits_table or r < 0 or c < 0:
        return False

    is_at_origin = r == 0 and c == 0

    if is_at_origin or path(r - 1, c) or path(r, c - 1):
        path_list.append((r, c))
        return True

    return False


path(40, 40)
print(path_list)
print(path_memo)
