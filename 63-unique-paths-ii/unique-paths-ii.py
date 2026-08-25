class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return 0
        m,n=len(grid),len(grid[0])
        dp=[0]*n
        dp[0]=1
        
        for r in range(m):
            for c in range(n):
                if r or c:
                    if grid[r][c]==1:
                        dp[c]=0
                    elif c>0:
                        dp[c]+=dp[c-1]
        return dp[-1]
