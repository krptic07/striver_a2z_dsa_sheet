def bubble_sort(array):
    for i in range(len(array) - 1, - 1, -1):
        max_element = array[i]
        max_element_index = i
        for j in range(i-1, -1, -1):
            if array[j] > max_element:
                max_element = array[j]
                max_element_index = j
        array[i], array[max_element_index] = array[max_element_index], array[i]
        if max_element_index == 0:
            print('er')
            return array
    return array

def recursive_bubble_sort(array, last_index):
    if last_index == 0:
        return array
    else:
        for j in range (last_index, -1, -1):
            max_element = array[last_index]
            max_element_index = last_index
            if (array[j] > max_element):
                max_element_index = j
                max_element = array[j]
        array[last_index], array[max_element_index] = array[max_element_index], array[last_index]
        return recursive_bubble_sort(array, last_index-1)

if __name__ == '__main__':
    unsorted_array = [13,46,24,52,20,9]
    print(bubble_sort(unsorted_array))
    print(recursive_bubble_sort(unsorted_array, len(unsorted_array)-1))