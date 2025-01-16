def selection_sort(array):
    for i in range(0, len(array)):
        min_element = array[i]
        min_element_index = i
        for j in range(i, len(array)):
            if array[j] < min_element:
                min_element = array[j]
                min_element_index = j
        array[i], array[min_element_index] = array[min_element_index], array[i]
    return array

if __name__ == '__main__':
    unsorted_array = [13,46,24,52,20,9]
    print(selection_sort(unsorted_array))