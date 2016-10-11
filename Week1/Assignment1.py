def get_list():
    """
    Create list of integers using IntegerArray.txt
    :return: list of integers
    """
    with open('IntegerArray.txt') as f:
        lon = []
        for line in f:
            lon.append([int(x) for x in line.split()][0])
    return lon


def count_inversions(lon, inv):
    if len(lon) < 2:
        return lon, 0
    else:
        mid = int(len(lon)/2)
        left_list, left_inv = count_inversions(lon[:mid], inv)
        right_list, right_inv = count_inversions(lon[mid:], inv)
        left_right_inv = left_inv + right_inv

        return count_split_inversions(left_list, right_list, left_right_inv)


def count_split_inversions(left, right, inversions):
    i = 0
    j = 0
    output_list = []

    for _ in range(0, len(left) + len(right)):
        if i == len(left):
            output_list.append(right[j])
            j += 1
        elif j == len(right):
            output_list.append(left[i])
            i += 1
        elif left[i] < right[j]:
            output_list.append(left[i])
            i += 1
        else:
            output_list.append(right[j])
            j += 1
            inversions += len(left) - i
    return output_list, inversions


lon = get_list()
print count_inversions(lon, 0)[1]

