# Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

def longest_subarray_sum_k(array, k):
    longest_subarray = 0
    for i in range(len(array)):
        long = 0
        if (array[i] == k):
            long += 1
            if (long > longest_subarray):
                longest_subarray = long
            continue
        sum = 0
        for j in range(i, len(array)):
            sum += array[j]
            if (sum == k):
                long = (j - i) + 1
                # longest_subarray += 1
                break
            if (sum > k):
                break
        if (long > longest_subarray):
            longest_subarray = long
    return longest_subarray

if __name__=="__main__":
    array = [1,-1,0]
    print(longest_subarray_sum_k(array, 0))

