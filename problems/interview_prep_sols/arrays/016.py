# not classic approaches are discussed here

def findMissingConsecutiveSum(arr):
    n = len(arr)
    S = ((n+2)*(n+2+1))//2
    Sd = sum(arr)
    avg = Sd//n

    sum_till_avg = (avg*(avg+1))//2
    sum_till_avg_in_array = sum([ele for ele in arr if ele<=avg])

    first = sum_till_avg - sum_till_avg_in_array  
    second = (S-Sd) - first
    return first, second



def findMissingConsecutiveXor(arr):
    n = len(arr)
    xor=arr[0]
    for i in range(1,n):
        xor^=arr[i]
    for i in range(1,n+3):
        xor^=i
    
    set_no=(xor) & ~(xor-1)

    x=0
    y=0
    for i in range(n):
        if arr[i] & set_no:
            x^=arr[i]
        else:
            y^=arr[i]
    for i in range(1,n+3):
        if i & set_no:
            x^=i
        else:
            y^=i
    return x,y

print(findMissingConsecutiveSum([1, 3, 5, 6]))
print(findMissingConsecutiveXor([1, 3, 5, 6]))