#sort and check udpate start and end indices
def findUnsortedSubarray(nums):
    snums = sorted(nums)
    start, end = len(nums), 0
    for i in range(len(nums)):
        if nums[i]!=snums[i]:
            start = min(start, i)
            end = max(end, i)
    return end-start+1 if end-start+1 >=0 else 0

def findUnsortedSubarray2(nums):
    mini, maxi = float("inf"), float("-inf")
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            mini = min(mini, nums[i])
    for i in range(len(nums)-2, -1, -1):
        if nums[i] > nums[i+1]:
            maxi = max(maxi, nums[i])
    
    for start in range(len(nums)):
        if nums[start]>mini:
            break
    for end in range(len(nums)-1, -1, -1):
        if nums[end] < maxi:
            break
    
    return end-start+1 if end-start+1 > 0 else 0

print(findUnsortedSubarray([1, 3, 3, 3, 2, 2, 2]))
print(findUnsortedSubarray2([1, 3, 3, 3, 2, 2, 2]))
