# Given a number ‘N’, find out the sum of the first N natural numbers.

def sum_of_numbers(n, sum):
    if(n<=0):
        return sum
    else:
        sum = sum + n
        n = n - 1
        return sum_of_numbers(n, sum)


if __name__ == "__main__":
    number = int(input("Please enter your number"))
    print(sum_of_numbers(number, 0))