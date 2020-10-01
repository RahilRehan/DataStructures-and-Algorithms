class Solution:
    # sum overflow problem
        # t.c is O(N)
    def missingNumber01(nums) -> int:
        n = len(nums) + 1
        return (n*(n-1))//2 - sum(nums)
    
    # xor solutions
    # t.c is O(N)
    def missingNumber02(nums]) -> int:
        xor = 0
        for ele in nums:
            xor ^= ele
        
        for i in range(0, len(nums)+1):
            xor ^= i        
        return xor

    #cyclic sort method, tortoise and hare
    # normal swap is not working, use this one for sure
    def swap(self, i, j, nums):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    def missingNumber03(nums]) -> int:
        for i in range(len(nums)):
            while nums[i] < len(nums) and nums[i]!=i:
                self.swap(i, nums[i], nums)
        for idx, ele in enumerate(nums):
            if idx!=ele:
                return idx
        return len(nums)