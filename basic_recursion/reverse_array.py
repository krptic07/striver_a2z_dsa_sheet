# You are given an array. The task is to reverse the array and print it. 

def reverse_array(array, i, j):
    if (i >= j):
        return array
    else:
        array[i], array[j] = array[j], array[i]
        return reverse_array(array, i+1, j-1)

if __name__ == "__main__":
    array = [1,2,3,4,5]
    print(reverse_array(array, 0, len(array) -1 ))