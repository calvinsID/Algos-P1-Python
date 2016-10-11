# Randomized Selection:
# Select ith smallest element of array

from random import randint


def random_select(unordered_list, ith):
    if len(unordered_list) < 2:
        return unordered_list[0]

    pivot_index = randint(0, len(unordered_list) - 1)
    new_pivot_index = partition(unordered_list, pivot_index)

    if new_pivot_index == ith - 1:
        return unordered_list[new_pivot_index]
    elif new_pivot_index < ith:
        return random_select(unordered_list[new_pivot_index + 1:], ith - new_pivot_index - 1)
    else:
        return random_select(unordered_list[:new_pivot_index], ith)


def partition(unordered_list, pivot_index):
    pivot = unordered_list[pivot_index]
    unordered_list[pivot_index], unordered_list[0] = unordered_list[0], unordered_list[pivot_index]

    i = 1
    for j in range(0, len(unordered_list)):
        if unordered_list[j] < pivot:
            unordered_list[i], unordered_list[j] = unordered_list[j], unordered_list[i]
            i += 1
    unordered_list[0], unordered_list[i-1] = unordered_list[i-1], unordered_list[0]
    return i-1


test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print random_select(test_arr, 3)
