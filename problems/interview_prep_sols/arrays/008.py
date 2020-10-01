def replaceElements(arr):
    mx = -1
    for idx in range(len(arr)-1, -1, -1):
        temp = arr[idx]
        arr[idx] = mx
        mx = max(arr[idx], temp)
    return arr

print(replaceElements([17,18,5,4,6,1]))