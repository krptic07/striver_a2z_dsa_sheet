#binary search
import math

def binary_search(array, number):
    left = 0
    right = len(array) - 1
    found = False
    while (left <=right):
        mid = math.floor((left + right) / 2)
        if array[mid] == number:
            found = True
            break
        elif array[mid] > number:
            right = mid - 1
        else: 
            left = mid + 1
    return found

def binary_search_decreasing(array, number):
    left = 0
    right = len(array) - 1
    found = False
    while (left <=right):
        mid = math.floor((left + right) / 2)
        if array[mid] == number:
            found = True
            break
        elif array[mid] > number:
            left = mid + 1
        else: 
            right = mid - 1
    return found

def recursive_binary(array, number, left, right):
    if (left >= right):
        return False  
    else:
        mid = math.floor((left + right)/2)
        if array[mid] == number:
            return True
        if array[mid] < number:
            return recursive_binary(array, number, mid+1, right)
        if array[mid] > number:
            return recursive_binary(array, number, left, mid-1)
        
if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9,10]
    print(binary_search(array, 6))
    print(recursive_binary(array, 6, 0, len(array) - 1))
    print(binary_search_decreasing([9,8,7,6,5,4,3,2,1],6))