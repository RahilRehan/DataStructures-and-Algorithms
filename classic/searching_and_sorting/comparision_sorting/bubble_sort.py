def buble_sort(arr):
	for i in range(len(arr)):
		swapped = False
		for j in range(len(arr)-i-1):
			if arr[j]>arr[j+1]:
				swapped = True
				arr[j], arr[j+1] = arr[j+1], arr[j]
		if not swapped:
			return arr
	return arr

# Bubble up max element to end in each step

# Time Complexity is O(N^2)
# Space Complexity is O(1)
# If array is sorted, T.C is O(N) as we are using "swapped" variable

print(buble_sort([6, 5, 3, 1, 8, 2, 4, 7]))