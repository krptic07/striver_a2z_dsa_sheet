#Given an array of N integers, left rotate the array by one place.

def shift_left_one_place(array):
    for i in range(len(array) - 2, -1, -1):
        array[i], array[len(array) - 1] = array[len(array) - 1], array[i]
    return array

if __name__ == '__main__':
    unsorted_array = [1,2,3,4,5,6,7,8,9]
    print(shift_left_one_place(unsorted_array))
        