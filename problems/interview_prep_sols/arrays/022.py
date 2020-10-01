#binary search approach O(MlogN)
def countNegativesBS(grid):
    
    def bs(nums):
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] < 0:
                end = mid -1
            else:
                start = mid + 1
        return len(nums) - start
        
    
    return sum([bs(row) for row in grid])

#Climbing approach O(M + N)
def countNegativesClimb(grid):
    count = 0
    n, m = len(grid), len(grid[0])
    i, j = n-1, 0
    while i>=0 and j<m:
        if grid[i][j] < 0:
            count += (m - j)
            i-=1
        else:
            j+=1
    return count

print(countNegativesBS([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))