# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
def singleNumber(nums) -> int:
    xor = 0
    for ele in nums:
        xor^=ele
    return xor
print(singleNumber([2, 1, 2, 3, 1]))


#  every element appears three times except for one, which appears exactly once. Find that single one.
def singleNumber2(nums):
    ans = 0
    
    for i in range(32):
        
        bit_sum = 0
        
        for ele in nums:
            bit_sum += (ele>>i) & 1
            
        ans |= (bit_sum%3)<<i
        
    if ( ans & (1 << 31) ) == 0:
        return ans
    else:
        return -( (ans^(0xFFFF_FFFF))+1 )

# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
def singleNumber3(nums):
    xor = 0
    for num in nums:
        xor ^= num
        
    for i in range(32):
        if xor & 1 << i:
            set_bit = i
            break
    
    a,b = 0, 0
    
    for num in nums:
        if num & 1 << set_bit:
            a ^= num
        else:
            b ^= num
    
    return a, b