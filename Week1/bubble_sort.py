# Bubble sort


def bubble(unsorted_arr):
    """

    Average time: n^2
    Worst time: n^2

    :param unsorted_arr: An unsorted array of numbers
    :return: Sorted array
    """

    end = len(unsorted_arr) - 1

    while (end != -1):

        swapped = -1

        for i in range(len(unsorted_arr)-1):
            if unsorted_arr[i] > unsorted_arr[i+1]:
                temp = unsorted_arr[i]
                unsorted_arr[i] = unsorted_arr[i+1]
                unsorted_arr[i+1] = temp
                swapped = i

        end = swapped


    print unsorted_arr



bubble([1, 5, 6, 2, 4])