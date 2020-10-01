def findPeakElement(nums):
    if not nums:
        return 0
    l, r = 0, len(nums)-1
    while l <= r:
        if l == r:
            return l
        mid = l + (r-l)//2
        if (mid-1 < 0 or nums[mid-1] < nums[mid]) and nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid] > nums[mid+1]:
            r = mid
        else:
            l = mid + 1