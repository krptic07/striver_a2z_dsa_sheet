# Given an integer N, return true it is an Armstrong number otherwise return false.
# An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
import math

def armstrong_number(n):
    number_of_digits = math.floor(math.log10(n) + 1)
    digit_string = str(n)
    total_sum = 0
    for i in range(0, len(digit_string)):
        total_sum = total_sum + int(digit_string[i])**number_of_digits
    return total_sum == n

if __name__ == "__main__":
    number = int(input("Please enter your number"))
    print(armstrong_number(number))


