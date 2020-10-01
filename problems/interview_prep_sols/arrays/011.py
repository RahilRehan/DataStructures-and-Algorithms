
def merge(arr, left, mid, right):
    i, j, k = 0, 0, 0
    count = 0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            count += (len(left)-i)
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return count

def merge_sort(arr):
    inversions = 0
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        inversions += merge_sort(left)
        inversions += merge_sort(right)
        inversions += merge(arr, left, mid, right)
    return inversions
        
print(merge_sort([8, 4, 2, 1]))
print(merge_sort([3, 1, 2]))
