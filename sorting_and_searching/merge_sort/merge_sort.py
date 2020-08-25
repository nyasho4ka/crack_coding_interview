import timeit
import random


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


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left_part = arr[:middle]
    right_part = arr[middle:]
    sorted_left = merge_sort(left_part)
    sorted_right = merge_sort(right_part)
    sorted_merge = merge(sorted_left, sorted_right)
    return sorted_merge


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    times = timeit.repeat(stmt=stmt, setup=setup_code, repeat=3, number=10)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


init_array = [random.randint(1, 1000) for _ in range(100000)]

run_sorting_algorithm("merge_sort", init_array)
