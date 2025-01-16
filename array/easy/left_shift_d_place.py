# Given an array of integers, rotating array of elements by k elements either left or right.

def reverse_array(array, left, right):
    while (left <= right):
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return

def shift_by_d_place_left(array, k):
    reverse_array(array,0,k)
    reverse_array(array,k+1, len(array) -1)
    reverse_array(array,0,len(array)-1)

def shift_by_d_place_right(array, k):
    reverse_array(array,0,len(array) - 1 - k)
    reverse_array(array,len(array) - k, len(array) -1)
    reverse_array(array,0,len(array)-1)

if __name__ == '__main__':
    unsorted_array = [1,2,3,4,5,6,7,8,9]
    shift_by_d_place_left(unsorted_array, 2)
    print(unsorted_array)
        