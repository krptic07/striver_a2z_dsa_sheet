# Given an integer N, return all divisors of N.
import math

def all_divisors(n):
    list_of_divisors = []
    loop_length = math.floor(math.sqrt(n)) + 1
    for i in range(1, loop_length):
        if n % i == 0:
            list_of_divisors.append(i)
            if n // i != i:
                list_of_divisors.append(n//i)
    list_of_divisors =  list_of_divisors
    return list_of_divisors


if __name__ == "__main__":
    number = int(input("Please enter your number"))
    print(all_divisors(number))

