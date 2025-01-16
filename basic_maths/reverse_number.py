# Given an integer N return the reverse of the given number.
import math

def reverse_number(n):
    reverse_number = 0
    while n > 0:
        last_digit = n % 10
        reverse_number = (reverse_number * 10) + last_digit
        n = n // 10
    return reverse_number   

if __name__ == "__main__":
    number = int(input("Please enter the number"))
    print(reverse_number(number))