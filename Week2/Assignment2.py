tally = 0


def get_list():
    """
    Create list of integers using QuickSort.txt
    :return: list of integers
    """
    with open('QuickSort.txt') as f:
        lon = []
        for line in f:
            lon.append([int(x) for x in line.split()][0])
    return lon


def quick_sort(unsorted_list, question_num):
    return quick_sort_this(unsorted_list, 0, len(unsorted_list)-1, question_num)


def quick_sort_this(unsorted_list, begin, end, question_num):
    global tally

    if end - begin == -1:
        return
    else:
        if question_num == 1:
            pivot_index = begin
        if question_num == 2:
            pivot_index = end
        if question_num == 3:
            pivot_index = median_pivot(unsorted_list, begin, end)
        unsorted_list[pivot_index], unsorted_list[begin] = unsorted_list[begin], unsorted_list[pivot_index]
        new_pivot_index = partition(unsorted_list, begin, end+1)
        quick_sort_this(unsorted_list, begin, new_pivot_index - 1, question_num)
        quick_sort_this(unsorted_list, new_pivot_index + 1, end, question_num)
    return


def partition(arr, left, right):
    global tally
    tally += right - left - 1

    pivot = arr[left]
    i = left + 1
    for j in range(left+1, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[left], arr[i-1] = arr[i-1], arr[left]
    return i-1


def median_pivot(arr, begin, end):
    median_index = (begin + end) / 2

    first = arr[begin]
    second = arr[median_index]
    third = arr[end]

    if first > second > third or first < second < third:
        return median_index
    if first > third > second or first < third < second:
        return end
    return begin


def main():
    global tally

    questions = [1, 2, 3]

    for i in questions:
        lon = get_list()
        tally = 0
        quick_sort(lon, i)
        print 'Question', i, ':', tally

    return


if __name__ == '__main__':
    main()