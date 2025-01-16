#  Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

def second_largest_smallest(array):
    i = 0
    j = len(array) - 1
    large = float("-inf")
    second_large = float("-inf")
    small = float("inf")
    second_small = float("inf")     
    while i <= len(array) - 1 and j >= 0:
        if (array[i] > large):
            second_large = large
            large = array[i]
        if (array[i] > second_large and array[i] != large):
            second_large = array[i]
        if (array[j] < small):
            second_small = small
            small = array[j]
        if (array[j] < second_small and array[j] != small):
            second_small = array[j]
        i += 1
        j -= 1
    return (second_large, second_small)


if __name__ == '__main__':
    unsorted_array = [13,46,24,52,20,9]
    print(second_largest_smallest(unsorted_array))