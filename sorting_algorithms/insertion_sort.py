def insertion_sort(array):
    for i in range(0, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j-1], array[j] = array[j], array[j-1]
    return array

def recursive_insertion_sort(array, last_index):
    if last_index == 0:
        return array
    else:
        for j in range(last_index, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
        return recursive_insertion_sort(array, last_index-1)

if __name__ == '__main__':
    unsorted_array = [13,46,24,52,20,9]
    print(insertion_sort(unsorted_array))
    print(recursive_insertion_sort(unsorted_array, len(unsorted_array) - 1))