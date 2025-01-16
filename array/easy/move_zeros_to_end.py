import math 

def create_map(array, most_prominent):
    number_map = {}
    prominent_list = []
    for i in range(0, len(array) - 1):
        if array[i] in number_map and array[i] != most_prominent:
            number_map[array[i]] +=1
        if array[i] not in number_map and array[i] != most_prominent:
            number_map[array[i]] = 1
        if array[i] in number_map and array[i] == most_prominent:
            prominent_list[0] =  prominent_list[0] + 1
            prominent_list[1].append(i)
        if array[i] not in number_map and array[i] == most_prominent:
            prominent_list =  [1,[i]]
    return (number_map, prominent_list)

def removing_prefix_suffix(array, number_map, prominent_list, count):
    values_list = number_map.values()
    keys_list = number_map.keys()
    max_number_freq = max(values_list) 
    if(prominent_list[0] > max_number_freq):
        return (count, "Done")
    else:
        max_number = keys_list[values_list.index(max_number_freq)]
        start = prominent_list[1][0]
        end = prominent_list[1][-1]
        max_number_left_count = 0
        max_number_right_count = 0
        for i in range(0, start):
            if array[i] == max_number:
                max_number_left_count += 1
        for j in range(end, len(array) - 1):
            if array[j] == max_number:
                max_number_right_count += 1
        if (max_number_left_count > max_number_right_count):
            array = array[0:start+1:1]
        if(max_number_right_count> max_number_left_count):
            array = array[end: -1: 1]
        return (count + 1, "No")

def main_function(array, most_prominent):
    number_map, prominent_list = create_map(array, most_prominent)
    count, status = removing_prefix_suffix(number_map, prominent_list)
    if status == "Done":
        return count
    else:
        return main_function(array, most_prominent)


if __name__ == "__main__":
    array = [1,2,4,3,4,4,3,5,6]
    print(create_map(array, 4))