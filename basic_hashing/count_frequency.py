#Given an array, we have found the number of occurrences of each element in the array.

def count_frequency(array):
    frequency_map = {}
    for i in range(0, len(array) - 1):
        if array[i] in frequency_map:
            frequency_map[array[i]] += 1
        else:
            frequency_map[array[i]] = 1
    return frequency_map

if __name__ == "__main__":
    array = [2, 8, 19, 24, 136]
    print(count_frequency(array))
    