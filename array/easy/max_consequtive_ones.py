# Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

def max_consequtive_ones(array):
    max_count = 0
    for i in range(len(array) - 1):
        if (array[i] == 0):
            continue
        if (array[i] == 1):
            j = i
            count = 0
            while (j <=len(array) -1):
                if(array[j] != 0):
                    count += 1
                    j += 1
                else:
                    break
            i = j
            if count > max_count:
                max_count = count
    if (max_count == 0 and array[-1] == 1):
        max_count += 1
    return max_count


if __name__=="__main__":
    array = [1, 0, 1, 0, 0, 1]
    print(max_consequtive_ones(array))




            