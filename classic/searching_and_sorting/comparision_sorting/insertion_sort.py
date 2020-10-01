def insertion_sort(arr):
	
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1

		while arr[j]>key and j>=0:
			arr[j+1] = arr[j]
			j-=1

		arr[j+1] = key

	return arr

# Time Complexity: O(N^2) and space Complexity is O(1)
# inplace, stable, online algorithm

print(insertion_sort([6, 5, 3, 1, 8, 2, 4, 7]))
