def increasingTriplet(nums):
    if len(nums) <= 2:
        return False
    mini, maxi = [], []
    _min, _max = float("inf"), float("-inf")
    for i in range(len(nums)):
        _min = min(_min, nums[i])
        mini.append(_min)
    
    for i in range(len(nums)-1, -1, -1):
        _max = max(_max, nums[i])
        maxi.insert(0, _max)
        
    for i in range(1, len(nums)-1):
        if mini[i-1] < nums[i] < maxi[i+1]:
            return True
    return False

# the most awesome solution, just look at how elif conditions are used.
def increasingTriplet2(nums):
    first, second = float("inf"), float("inf")
    for ele in nums:
        if ele <= first:
            first = ele
        elif ele <= second:
            second = ele
        else:
            return True
    return False