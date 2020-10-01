def selection_sort(arr):
	for i in range(len(arr)):
		min_index = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[min_index]:
				min_index = j
		arr[i], arr[min_index] = arr[min_index], arr[i]
	return arr

# Time complexity is O(N^2)
# Space complexity is O(1)

print(selection_sort([6, 5, 3, 1, 8, 7, 2, 4]))