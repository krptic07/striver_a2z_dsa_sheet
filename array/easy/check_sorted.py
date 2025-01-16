# Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

def check_sorted(array):
    for i in range(1, len(array) - 1):
        if (array[i] < array[i-1]):
            return False
    return True

if __name__ == '__main__':
    unsorted_array = [13,46,24,52,20,9]
    print(check_sorted(unsorted_array))