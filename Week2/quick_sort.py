# Quick sort

from random import randint


def quick_sort(unsorted_list):
    """
    Average time: n log(n)
    Worst time: n log(n)

    :param unsorted_list: An unsorted list of items
    :return: The list sorted
    """
    return quick_sort_this(unsorted_list, 0, len(unsorted_list)-1)


def quick_sort_this(unsorted_list, begin, end):
    """

    :param unsorted_list: An unsorted list of items
    :param begin: index of first element to sort
    :param end: index of last element to sort
    :return: The list sorted
    """
    if end - begin == -1:
        return
    else:
        pivot_index = randint(begin, end)

        unsorted_list[pivot_index], unsorted_list[begin] = unsorted_list[begin], unsorted_list[pivot_index]
        new_pivot_index = partition(unsorted_list, begin, end+1)

        quick_sort_this(unsorted_list, begin, new_pivot_index - 1)
        quick_sort_this(unsorted_list, new_pivot_index + 1, end)

    return unsorted_list


def partition(arr, left, right):
    """

    Running time: O(n) where n = right - left + 1

    :param arr: Array to be sorted
    :param left: index of leftmost element in the array that we have to look at
    :param right: index of rightmost element in the array that we have to look at + 1
    :return: index of pivot element
    """
    pivot = arr[left]
    i = left + 1
    for j in range(left+1, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # reposition pivot
    arr[left], arr[i-1] = arr[i-1], arr[left]
    return i-1


test_arr = [1, 3, 5, 7, 9, 8, 6, 4, 2]
print quick_sort(test_arr)
