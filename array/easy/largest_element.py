#Given an array, we have to find the largest element in the array.

def largest_element(array):
    max_element = array[0]
    for i in range(0, len(array) - 1):
        if (array[i] > max_element):
            max_element = array[i]
    return max_element


if __name__ == '__main__':
    unsorted_array = [13,46,24,52,20,9]
    print(largest_element(unsorted_array))