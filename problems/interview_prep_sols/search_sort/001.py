def findKthLargest(nums):
    heap = []
    for ele in nums:
        if len(heap) < k:
            heapq.heappush(heap, ele)
        else:
            heapq.heappushpop(heap, ele)
    return heapq.heappop(heap)