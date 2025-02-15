def partition(array, low, high):
    pivot_element = array[low] #taking first element as the pivot element, can be any random
    i = low
    j = high
    while(i < j):
        while (array[i] <= pivot_element and i <= high -1):
            i += 1
        while (array[j] >= pivot_element and j >= low + 1):
            j -= 1
        if (i < j):
            array[j], array[i] = array[i], array[j]
    array[low], array[j] = array[j], array[low]
    return j  


def quickSort(array, low, high):
    if(high<=low):
        return
    else:
        partitionIndex = partition(array, low, high)
        quickSort(array, low, partitionIndex-1)
        quickSort(array, partitionIndex+1, high)


if __name__ == '__main__':
    unsorted_array = [2,0,2,1,1,0]
    quickSort(unsorted_array, 0, len(unsorted_array) - 1)
    print(unsorted_array)