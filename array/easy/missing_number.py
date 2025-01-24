# Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array.

def missing_number(array):
    temp_array = []
    j = 1
    for i in range(len(array)):
        if array[i] == j:
            j +=1
        else:
            while j <= array[i]:
                if(j < array[i]):
                    temp_array.append(j)
                j +=1 
    return temp_array

def missing_number(array, n):
    xor1 = 0
    xor2 = 0
    for i in range(n - 1):
        xor2 = xor2 ^ array[i]  # XOR of array elements
        xor1 = xor1 ^ (i + 1)  # XOR up to [1...N-1]

    xor1 = xor1 ^ n  # XOR up to [1...N]

    return xor1 ^ xor2


if __name__=="__main__":
    array = [1,2,3,5,8,9,14]
    print(missing_number(array))



