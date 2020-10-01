def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def findTwoRepeatingElementsAlgebra(arr):
    from math import sqrt

    n = len(arr)
    l = n-2

    given_arr_sum = sum(arr)
    given_arr_prod = 1
    for ele in arr:
        given_arr_prod *= ele

    n_sum = (l*(l+1))//2
    n_prod = factorial(l)

    x_plus_y = given_arr_sum - n_sum
    x_mul_y = given_arr_prod//n_prod

    x_minus_y = sqrt((x_plus_y)**2 - 4*x_mul_y)

    x = int((x_plus_y - x_minus_y)//2)
    y = int(x_plus_y - x)

    return x, y

def findTwoRepeatingElementsXor(arr):
    n = len(arr)
    xor = 0
    for ele in arr:
        xor ^= ele
    for ele in range(1, n-1):
        xor ^= ele
    
    set_bit = xor & ~(xor-1)

    x, y = 0, 0
    for ele in arr:
        if ele&set_bit:
            x^=ele
        else:
            y^=ele
    for ele in range(1, n-1):
        if ele&set_bit:
            x^=ele
        else:
            y^=ele
    return x, y
     


print(findTwoRepeatingElementsAlgebra([2, 4, 3, 1, 2, 5, 4]))
print(findTwoRepeatingElementsXor([2, 4, 3, 1, 2, 5, 4]))


