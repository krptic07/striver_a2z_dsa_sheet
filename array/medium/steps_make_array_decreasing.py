# You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.

#Return the number of steps performed until nums becomes a non-decreasing array.

def totalSteps(nums):
        is_ascending = False
        steps = 0
        while is_ascending == False:
            deletion_index = []
            i = 1
            while i <= len(nums) - 1:
                if nums[i] == 'X':
                    j = i
                    while j < len(nums) - 1 and nums[j] == 'X':
                        j += 1
                    if j != len(nums) - 1:
                        if nums[j] < nums[i-1]:
                            deletion_index.append(j)
                            i = j + 1
                            continue
                        else:
                            i += 1
                            continue
                    if j == len(nums) - 1 and nums[j] == 'X':
                        break
                    if j == len(nums) - 1 and nums[j] != 'X':
                        if nums[j] < nums[i-1]:
                            deletion_index.append(j)
                        break
                if nums[i] != 'X':
                    if (nums[i-1] > nums[i]):
                        deletion_index.append(i)
                    i += 1
            if (len(deletion_index) == 0):
                is_ascending = True
            else:
                steps += 1
                for i in range(len(deletion_index)):
                    nums[deletion_index[i]] = 'X'
        return steps

if __name__=="__main__":
    array = [5,3,4,4,7,3,6,11,8,5,11]
    print(totalSteps(array))

