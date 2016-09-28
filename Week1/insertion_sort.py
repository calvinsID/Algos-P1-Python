# Insertion sort


def insertion(unsorted_arr):
    """
    Average time: n^2
    Worst time: n^2

    :param unsorted_arr: An unsorted array of numbers
    :return: Sorted array
    """

    for index in range(len(unsorted_arr)) :
        insert_val = unsorted_arr[index]
        posn = index

        while posn > 0 and insert_val < unsorted_arr[posn - 1]:
            unsorted_arr[posn] = unsorted_arr[posn-1]
            unsorted_arr[posn-1] = insert_val
            posn -= 1

    return unsorted_arr

unsorted = [5, 3, 8, 9, 1]
print insertion(unsorted)