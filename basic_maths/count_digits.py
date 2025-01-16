# Given an integer N, return the number of digits in N.

import math

def count_digits(n):
    count = int(math.log10(n) + 1)
    return count

if __name__ == "__main__":
    number = int(input("Please enter your number"))
    print(count_digits(number))

