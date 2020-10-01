def majorityElement(nums) -> int:
    vote = 0
    maj = nums[0]
    for ele in nums:
        if ele == maj:
            vote+=1
        else:
            vote-=1
            if vote == 0:
                maj = ele
                vote = 1
    return maj

print(majorityElement([2,2,1,1,1,2,2]))