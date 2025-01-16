def merge(array, low, high):
    left = low
    mid = (low + high)//2
    right = mid + 1
    temp_array = []
    while left <= mid and right <= high:
        if array[left] < array[right]:
            temp_array.append(array[left])
            left +=1
        else:
            temp_array.append(array[right])
            right +=1
    
    while left <= mid:
        temp_array.append(array[left])
        left += 1
    while right <= high:
        temp_array.append(array[right])
        right += 1
    for i in range(low, high + 1):
        array[i] = temp_array[i - low]
    return array

def merge_sort(array, low, high):
    if low >= high:
        return array
    else:
        mid = (low + high) // 2
        merge_sort(array, low, mid)
        merge_sort(array, mid+1, high)
        return merge(array, low, high)

if __name__ == '__main__':
    unsorted_array = [13,46,24,52,20,9]
    print(merge_sort(unsorted_array, 0 , len(unsorted_array)-1))