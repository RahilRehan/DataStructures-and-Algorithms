# slide explaining partition function
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/video-lectures/lecture-4-quicksort-randomized-algorithms/lec4.pdf

def partition(arr, p, r):
	pivot = arr[p]
	i = p
	# we can follow this approach or two pointer approach, https://www.youtube.com/watch?v=7h1s2SojIRw
	for j in range(p+1, r+1):
		if arr[j]<pivot:
			i+=1
			arr[i], arr[j] = arr[j], arr[i]
	arr[p], arr[i] = arr[i], arr[p]
	return i

def quicksort(arr, p, r):
	if p<r:
		q = partition(arr, p, r)
		quicksort(arr, p, q-1)
		quicksort(arr, q+1, r)
	return arr

arr = [6, 5, 3, 1, 8, 7, 2, 4]
print(quicksort(arr, 0, len(arr)-1))

# Worst case is O(N^2) -> try to pick pivot randomly to bring down T.C to O(NlogN)
# Space complexity is O(1)
