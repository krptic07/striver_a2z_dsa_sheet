# Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

def single_frequency_number(array):
    frequency_map = {}
    for i in range(len(array)):
        if array[i] in frequency_map:
            frequency_map[array[i]] += 1
        else:
            frequency_map[array[i]] = 1
    keys = list(frequency_map.keys())
    values = list(frequency_map.values())

    return keys[values.index(1)]

def using_xor(array):
    xor = 0
    for i in range(len(array)):
        xor = xor ^ array[i]
    return xor

if __name__=="__main__":
    array = [4,1,2,1,2]
    print(single_frequency_number(array))
    print(using_xor(array))

