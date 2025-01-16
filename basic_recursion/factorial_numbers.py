# Given a number X,  print its factorial.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
if __name__ == "__main__":
    number = int(input("Please enter your number"))
    print(factorial(number))