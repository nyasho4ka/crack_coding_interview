import random
import timeit


def insertion_sort(array, left=0, right=None):
    right = right if right else len(array) - 1

    for i in range(left+1, right+1):
        key_item = array[i]

        j = i - 1

        while j >= left and key_item < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array


def merge(arr1, arr2):
    # create a list with size len(arr1) + len(arr2)
    result = [0] * (len(arr1) + len(arr2))
    i = 0
    j = 0
    for k in range(len(result)):
        if i >= len(arr1):
            result[k] = arr2[j]
            j += 1
            continue
        if j >= len(arr2):
            result[k] = arr1[i]
            i += 1
            continue
        if arr1[i] < arr2[j]:
            result[k] = arr1[i]
            i += 1
        elif j < len(arr2):
            result[k] = arr2[j]
            j += 1

    return result


def timsort(array, min_run=32):
    n = len(array)

    for i in range(0, n, min_run):
        insertion_sort(array, i, min(i + min_run - 1, n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size*2):
            # get midpoint
            midpoint = start + size
            endpoint = min(start + size * 2, n)
            merged = merge(
                array[start:midpoint],
                array[midpoint:endpoint]
            )
            array[start:endpoint] = merged

        size *= 2

    return array


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    times = timeit.repeat(stmt=stmt, setup=setup_code, repeat=3, number=10)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


init_array = [random.randint(1, 1000) for _ in range(100000)]

run_sorting_algorithm("timsort", init_array)
