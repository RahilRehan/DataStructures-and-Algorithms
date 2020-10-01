t = int(input())
import heapq as hq
while t:
    n, k = list(map(int, input().split()))
    li = list(map(int, input().split()))
    heap = []
    output = []
    for ele in li:
        if len(heap) <= k+1:
            hq.heappush(heap, ele)
        else:
            output.append(hq.heappushpop(heap, ele))
    while heap:
        output.append(hq.heappop(heap))
    print(*output)
    t-=1