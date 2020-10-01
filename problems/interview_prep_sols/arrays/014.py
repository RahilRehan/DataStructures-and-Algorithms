# Classic Approach
def maxSubArray1(nums):
    cur_max, glob_max = nums[0], nums[0]
    for i in range(1, len(nums)):
        cur_max = max(nums[i], cur_max + nums[i])
        glob_max = max(glob_max, cur_max)
    return glob_max

# dp approach
def maxSubArray2(nums):
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i-1]+nums[i])
    return max(nums)

# sliding window
def maxSubArray(nums):
    result = nums[0]
    start, end, cs = 0,0,0
    for end in range(len(nums)):
        cs += nums[end]
        result = max(result, cs)
        if cs < 0:
            cs = 0
            start = end
    return result

