#You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.

def move_zeros_to_end(array):
    for i in range(0, len(array) - 1):
        if (array[i] != 0):
            continue
        else:
            if (array[i+1] != 0):
                array[i], array[i+1] = array[i+1], array[i] #swap the adjancent zero and non-zero
                continue
            else:
                for j in range(i+1, len(array)):
                    if (array[j] != 0): # found first non-zero in continuos zeros
                        break
                if (j == len(array) -1 and array[j] == 0):
                    break
                elif (j == len(array) - 1 and array[j] !=0): #last element is non zero
                    array[j], array[i] = array[i], array[j]
                    break
                else:
                    array[j], array[i] = array[i], array[j] #swap  first non-zero in continuos zeros
    return array

    
if __name__ == "__main__":
    array = [1,0,2,3,0,0,0,4,0,1]
    print(move_zeros_to_end(array))