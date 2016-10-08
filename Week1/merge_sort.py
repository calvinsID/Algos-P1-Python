# Merge sort


def merge_sort(unsorted_list):
    """
    Average time: n log(n)
    Worst time: n log(n)

    :param unsorted_list: An unsorted list of numbers
    :return: The list sorted
    """

    if len(unsorted_list) < 2:
        return unsorted_list
    else:
        mid = int(len(unsorted_list)/2)
        left = merge_sort(unsorted_list[:mid])
        right = merge_sort(unsorted_list[mid:])
        return merge(left, right)


def merge(left_list, right_list):
    i = 0
    j = 0
    output_list = []

    for _ in range(0, len(left_list) + len(right_list)):
        if i == len(left_list):
            output_list.append(right_list[j])
            j += 1
        elif j == len(right_list):
            output_list.append(left_list[i])
            i += 1
        elif left_list[i] < right_list[j]:
            output_list.append(left_list[i])
            i += 1
        else:
            output_list.append(right_list[j])
            j += 1
    return output_list


print merge_sort([7, 6, 4, 3, 1])



