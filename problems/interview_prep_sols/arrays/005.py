def smallerNumbersThanCurrent(nums):
    bucket = [0] * 101
    for num in nums:
        bucket[num] += 1
        
    accu = [0] * 101
    for i in range(1, 101):   # 1 ~ 100
        accu[i] = accu[i-1] + bucket[i-1]
        
    return [ accu[num] for num in nums ]

print(smallerNumbersThanCurrent([8,1,2,2,3]))