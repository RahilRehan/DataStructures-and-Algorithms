def firstMissingPositive(nums):
    result = 1
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == result:
            result += 1
    return result

def firstMissingPositivecyclic(nums):
    for i in range(len(nums)):
        while nums[i]>0 and nums[i] <= len(nums) and nums[i]!=nums[nums[i]-1]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

    for i in range(len(nums)):
        if nums[i]!=i+1:
            return i+1
        
    return len(nums)+1

def firstMissingPositiveBit(nums):
    n = len(nums)
    
    # mark those elements who aren't in the range of [1, n]
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    
    # mark visited elements as negative
    for i in range(n): 
        if (abs(nums[i]) - 1 < n and nums[abs(nums[i]) - 1] > 0): 
            nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1] 

    # find first positive/unmarked element and return its index
    for i in range(n): 
        if (nums[i] > 0): 
            return i + 1
    
    # if all elements are negative/marked means all elements are in the range of [1, n]
    return n + 1