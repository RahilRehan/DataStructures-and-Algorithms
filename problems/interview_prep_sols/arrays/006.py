def sortArrayByParity(A):
    
    left, right = 0, len(A)-1
    
    while left < right:
        if A[left]&1:
            A[left], A[right] = A[right], A[left]
            right -=1
        else:
            left+=1
    return A

print(sortArrayByParity([3,1,2,4]))