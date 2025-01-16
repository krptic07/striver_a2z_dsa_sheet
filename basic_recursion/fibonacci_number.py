# Given an integer N. Print the Fibonacci series up to the Nth term.

def fibonacci_number(n, array):
    if n == 0:
        return [0]
    else:
        if array[len(array) - 1] == n:          
            return array
        else:
            last_index = len(array) - 1
            next_element = array[last_index - 1] + array[last_index]
            array.append(next_element)
            return fibonacci_number(n, array)
        
if __name__ == "__main__":
    number = int(input("Please enter your number"))
    fibonacci_numbers = fibonacci_number(number, [0, 1])
    for i in range(0, len(fibonacci_numbers)):
        print(fibonacci_numbers[i], end=" ")
