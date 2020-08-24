def magic_index_distinct(sorted_array, start, end):
    if len(sorted_array) == 0 or start > end:
        return -1
    mid_index = (start + end) // 2
    if sorted_array[mid_index] == mid_index:
        return mid_index
    if sorted_array[mid_index] > mid_index:
        return magic_index_distinct(sorted_array, start, mid_index - 1)
    if sorted_array[mid_index] < mid_index:
        return magic_index_distinct(sorted_array, mid_index+1, end)


print(magic_index_distinct([-1, -2, -3, -4, -5, -6, -7, -8, -9, 9], 0, 9))
