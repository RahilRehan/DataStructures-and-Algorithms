#inplace using reverse
def rotate(nums, k)->None:
    n = len(nums)
    k = k%n
    def reverse(nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    reverse(nums, 0, n-k-1)
    reverse(nums, n-k, n-1)
    reverse(nums, 0, n-1)

rotate([1,2,3,4,5,6,7], 3)