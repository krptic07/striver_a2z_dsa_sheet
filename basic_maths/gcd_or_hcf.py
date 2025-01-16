# Given two integers N1 and N2, find their greatest common divisor.

# The Euclidean Algorithm is a method for finding the greatest common divisor of two numbers.
#  It operates on the principle that the GCD of two numbers remains the same even if the smaller number is subtracted from the larger number.

def gcd_using_eucledian(n1, n2):
    # if(n1 == 0):
    #     return n2
    # if(n2 == 0):
    #     return n1
    # else:
    #     min_number = min(n1, n2)
    #     if(min_number == n1):
    #         return gcd_using_eucledian(n1, n2-n1)
    #     if(min_number == n2):
    #         return gcd_using_eucledian(n1-n2, n2)
    while n1 > 0 and n2 > 0:
        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1
    if n1 == 0:
        return n2
    return n1
        

if __name__ == '__main__':
    n1 = int(input("your first number"))
    n2 = int(input("your second number"))
    print(f"gcd of {n1} and {n2} is {gcd_using_eucledian(n1,n2)}")