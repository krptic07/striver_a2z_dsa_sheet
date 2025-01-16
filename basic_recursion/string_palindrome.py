# "Given a string, check if the string is palindrome or not."
def palindrome_string(string):
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        else:
            start = start + 1
            end = end - 1
    return True

if __name__ == "__main__":
    string = input("Please enter your string")
    print(palindrome_string(string))