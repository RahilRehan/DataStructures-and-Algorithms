def cyclic_sort(nums):
    n = len(nums)
    # 0 based indexed cyclic sort
    for i in range(n):
        while nums[i] < len(nums) and nums[i]!=i: # add any other conditions you would like to a/c to the problem
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    
    #now check for "duplicates", "missing" etx
    for idx, ele in enumerate(nums):
        if idx!=ele: # check idx ac to the problem
            return idx
    return len(nums)
