import time


def get_power_set(elems):
    if len(elems) == 0:
        return ((), )
    elems = tuple(elems)
    result = {elems}

    for i in range(len(elems)):
        req = get_power_set(elems[:i] + elems[i + 1:])
        result.update(req)

    return result


print(get_power_set([1, 2, 3, 4]))
