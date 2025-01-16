#  Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

# If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.


def remove_duplicates(array):
    i = 0
    for j in range(1, len(array) - 1):
        if(array[j] != array[i]):
            i += 1
            array[i] = array[j]
    return array

if __name__ == '__main__':
    unsorted_array = [1,1,2,2,2,3,4,5,6,6,6,6,6,7,7,8,9,9,9,10,10]
    print(remove_duplicates(unsorted_array))
        