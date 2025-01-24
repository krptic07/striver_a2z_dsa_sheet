import math

def square_root_binary_search(number):
    left = 0
    right = 10 #upto what number square root we want to find, here its till 10*10 = 100
    ans = number
    while (left <= right):
        mid = math.floor((left+right)/2)
        if(mid*mid*mid <= number):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans

if __name__ == "__main__":
    number = int(input("Enter Number"))
    print(square_root_binary_search(number))