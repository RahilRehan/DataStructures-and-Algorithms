def merge(intervals):
    if len(intervals)<2:
        return intervals
    intervals.sort(key=lambda x:x[0])
    ans = []
    for idx, ele in enumerate(intervals):
        if idx == 0:
            ans.append(ele)
        top = ans[-1]
        if top[1]>=ele[0]:
            ans[-1] = [top[0], max(top[1], ele[1])]
        else:
            ans.append(ele)
    return ans
print(merge([[1,3],[2,6],[8,10],[15,18]]))