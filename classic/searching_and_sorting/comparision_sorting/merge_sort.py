def merge(arr, left, right):
	i, j, k = 0, 0, 0
	while i<len(left) and j<len(right):
		if left[i]<right[j]:
			arr[k] = left[i]
			i+=1
		else:
			arr[k] = right[j]
			j+=1
		k+=1

	while i<len(left):
		arr[k] = left[i]
		i+=1
		k+=1

	while j<len(right):
		arr[k] = right[j]
		j+=1
		k+=1

def merge_sort(arr):
	if len(arr)>1:
		mid = len(arr)//2
		left = arr[:mid]
		right = arr[mid:]
		merge_sort(left)
		merge_sort(right)
		merge(arr, left, right)

# Time complexity is O(NlogN) because there are logN levels and in each level we are comparing and modifiying N elements
# Space complexity is O(N) as at each level we have new arrays of size N combined.

arr = [6, 5, 3, 1, 8, 7, 2, 4]
merge_sort(arr)
print(arr)