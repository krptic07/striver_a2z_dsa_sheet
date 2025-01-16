# Given an integer N, check whether it is prime or not.
import math

def prime_number(n):
    loop_length = math.floor(math.sqrt(n)) + 1
    for i in range (1, loop_length):
        if n % i == 0 and i != 1 and i != n:
            return False
    return True

if __name__ == "__main__":
    number = int(input("Please enter your number"))
    print(prime_number(number))
