def productExceptSelf(nums):
    output = []
    product = 1
    for i in range(len(nums)):
        output.append(product)
        product *= nums[i]

    product = 1
    for i in range(len(nums)-1, -1, -1):
        output[i] *= product
        product *= nums[i]
    return output

print(productExceptSelf([1, 2, 3, 4]))