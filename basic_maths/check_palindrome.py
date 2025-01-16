#Given an integer N, return true if it is a palindrome else return false.
import math

def check_palindrome(n):
    reverse_number = 0
    copied_number = n 
    while n > 0:
        last_number = n % 10
        n = math.floor(n / 10)
        reverse_number = (reverse_number * 10) + last_number
    return copied_number == reverse_number

if __name__ == '__main__':
    input_number = int(input("Please enter your number"))
    print('your number is a palindrome', check_palindrome(input_number))

