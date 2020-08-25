import timeit
import random


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    # take pivot point
    rand_index = random.randint(0, len(arr) - 1)
    pivot = arr[rand_index]

    # low arr
    low = []
    # high arr
    high = []
    # same
    same = []

    for elem in arr:
        if elem < pivot:
            low.append(elem)
        elif elem > pivot:
            high.append(elem)
        else:
            same.append(elem)

    return quick_sort(low) + same + quick_sort(high)


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    times = timeit.repeat(stmt=stmt, setup=setup_code, repeat=3, number=10)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


init_array = [random.randint(1, 1000) for _ in range(100000)]

run_sorting_algorithm("quick_sort", init_array)
