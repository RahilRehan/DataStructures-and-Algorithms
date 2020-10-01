def maxProduct(self, A):
    res = A[0]
    # imax/imin stores the max/min product of
    # subarray that ends with the current number A[i]
    imax, imin = A[0], A[0]

    for i in range(1, len(A)):

        # multiplied by a negative makes big number smaller, small number bigger
        # so we redefine the extremums by swapping them
        if A[i] < 0:
            imax, imin = imin, imax

        # max/min product for the current number is either the current number itself
        # or the max/min by the previous number times the current one
        imax = max(A[i], imax*A[i])
        imin = min(A[i], imin*A[i])

        # the newly computed max value is a candidate for our global result
        res = max(res, imax)

    return res

def maxProduct2(nums):
	mini, maxi, res = 1, 1, -math.inf
	for n in nums:
		a = mini * n
		b = maxi * n
		mini = min(a, b, n)
		maxi = max(a, b, n)
		res = max(res, maxi)
	return res
