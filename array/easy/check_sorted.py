# Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

def check_sorted(array):
    for i in range(1, len(array) - 1):
        if (array[i] < array[i-1]):
            return False
    return True



if __name__ == '__main__':
    unsorted_array = [13,46,24,52,20,9]
    print(check_sorted(unsorted_array))

# cook your dish here
# def totalSteps(s):
#     originalString = "ADVITIYA"
#     totalSteps = 0
#     for i in range(0, len(originalString)):
#         if(- ord(s[i]) + ord(originalString[i]) > 0):
#             totalSteps +=  - ord(s[i]) + ord(originalString[i])
#         elif(- ord(s[i]) + ord(originalString[i]) < 0):
#             totalSteps +=  26 + (- ord(s[i]) + ord(originalString[i]))
#     return totalSteps
    
# if __name__ == "__main__":
#     print(totalSteps('ADVITIAA'))