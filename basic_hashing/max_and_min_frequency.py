# Given an array of size N. Find the highest and lowest frequency element.

def count_frequency(array):
    frequency_map = {}
    for i in range(0, len(array)):
        if array[i] in frequency_map:
            frequency_map[array[i]] += 1
        else:
            frequency_map[array[i]] = 1
    return frequency_map

def max_and_min_element(array):
    hash_map = count_frequency(array)

    values = hash_map.values()
    min_frequency = min(values)
    for key in hash_map.keys():
        if hash_map[key] == min_frequency and type(key) is int:
            print(f"min frequency {min_frequency} is of {key}")
    return

if __name__ == "__main__":
    array = [2, 8, 19, 24, 136]
    print(max_and_min_element(array))
    