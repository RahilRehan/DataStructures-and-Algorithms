def threeSum(arr):
    arr.sort()
    ans = set()
    for i in range(len(arr)-2):
        if arr[i]>0:
            break
        if i>0 and arr[i]==arr[i-1]:
            continue
        l = i+1 
        r = len(arr)-1
        while(l<r):
            _sum = arr[i]+arr[l]+arr[r]
            if _sum==0:
                ans.add((arr[i], arr[l], arr[r]))
            if _sum<=0:
                l+=1
            if _sum>0:
                r-=1
    return ans