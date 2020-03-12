class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[grid[0][0]]*len(grid[0]) for _ in range(len(grid))]
        for j in range(1,len(grid)):
            dp[j][0] = grid[j][0] + dp[j-1][0]
            
        
        for i in range(1, len(grid[0])):
            dp[0][i] = grid[0][i] + dp[0][i-1]
            
        
        
        for m in range(1, len(grid)):
            for n in range(1, len(grid[0])):
                dp[m][n] = grid[m][n] + min(dp[m-1][n], dp[m][n-1])
                
                
        return dp[len(grid) - 1][len(grid[0]) - 1]
