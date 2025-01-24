# Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

def union_sorted_array(array1, array2):
    i = 0
    j = 0
    temp_array = []
    while i <= len(array1) - 1 and j <= len(array2) - 1:
        if i != len(array1) - 1 and j != len(array2) - 1:
            if array1[i] == array1[i+1] or array2[j] == array2[j+1]:
                if array2[j]==array2[j+1]:
                    j +=1
                if array1[i] == array1[i+1]:
                    i +=1
                continue
        if array1[i] == array2[j]:
            temp_array.append(array2[j])
            i += 1
            j += 1
            continue
        if array1[i] < array2[j]:
            temp_array.append(array1[i])
            i +=1
            continue
        if array1[i] > array2[j]:
            temp_array.append(array2[j])
            j +=1
            continue
    if i >= len(array1):            
        for k in range(j, len(array2)):
            if temp_array[-1] == array2[k]:
                k +=1
                continue
            temp_array.append(array2[k])
        return temp_array
    if j >= len(array2):
        for k in range(i, len(array1)):
            if temp_array[-1] == array1[k]:
                k +=1
                continue
            temp_array.append(array1[k])
        return temp_array
    
def find_union(arr1, arr2):
    s = set()
    union = []
    
    for num in arr1:
        s.add(num)
    
    for num in arr2:
        s.add(num)
    
    for num in s:
        union.append(num)
    
    return union


def find_union_dict(arr1, arr2):
    freq = {}
    union = []
    
    for num in arr1:
        freq[num] = freq.get(num, 0) + 1
    
    for num in arr2:
        freq[num] = freq.get(num, 0) + 1
    
    for num in freq:
        union.append(num)
    
    return union

    
if __name__ == "__main__":
    array1 = [1,2,3,4,5]
    array2 = [2,3,4,4,5]
    print(union_sorted_array(array1, array2))

# if __name__ == "__main__":
#     t = int(input())
#     for _ in range(t):
#         n, m = map(int, input().split())
#         arr1 = list(map(int, input().split()))
#         arr2 = list(map(int, input().split()))

#         result = find_union(n, m, arr1, arr2)
#         print(" ".join(map(str, result)))