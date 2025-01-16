# Given a positive integer N, print the digits of N separately.
import math

def extract_digits(n):
    digits = []
    while n>0:
        digits.append(n%10)
        n = math.floor(n / 10)
    digits.reverse()
    return digits

if __name__ == "__main__":
    number = int(input("Please enter the number"))
    print(extract_digits(number))