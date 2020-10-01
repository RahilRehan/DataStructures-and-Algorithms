def sort_colors(nums):
    left, cur, right = 0, 0, len(nums)-1
    while (cur <= right):
        if nums[cur] == 1:
            cur += 1
        elif nums[cur] == 0:
            nums[cur], nums[left] = nums[left], nums[cur]
            cur += 1
            left += 1
        else:
            nums[cur], nums[right] = nums[right], nums[cur]
            right -= 1
    return nums

print(sort_colors([2,0,2,1,1,0]))