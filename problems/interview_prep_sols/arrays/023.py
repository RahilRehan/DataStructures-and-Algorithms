# Naive O(MN + MlogM) => O(M(N + logM))

def kWeakestRows(mat, k):
	temp = [(sum(row), idx) for idx, row in enumerate(mat)]
	temp.sort(key = lambda x:x[0])
	result = [ele for t, ele in temp][:k]
	return result


#Binary search + Sort. T.C => O(MlogN+MlogM) => O(M(logN + logM)) => O(MlogNM)

def kWeakestRows(mat, k):
def binary_search(row):
    start, end = 0, len(row)-1
    while start <= end:
        mid = start + (end - start)//2
        if row[mid] == 0:
            end = mid -1
        else:
            start = mid + 1
    return end + 1

result = sorted([(binary_search(row), idx) for idx, row in enumerate(mat)])[:k]
return [ele[1] for ele in result]


#Binary Search + Priority Queue(Heapq) => O(MlogN + MlogK + KlogK)

def kWeakestRows(mat, k):
	def binary_search(row):
		start, end = 0, len(row)-1
		while start <= end:
			mid = start + (end - start)//2
			if row[mid] == 0:
				end = mid -1
			else:
				start = mid + 1
		return end + 1

	return [i for count, i in nsmallest(k, ((binary_search(row), i) for i, row in enumerate(mat)))]