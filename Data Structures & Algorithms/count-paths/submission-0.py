class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = [[-1] * n for _ in range(m)]

        def dfs(r, c):
            
            if r == (m - 1) or c == (n - 1):
                return 1
            
            if r >= m or c >= n:
                return 0
            
            if memo[r][c] != -1:
                return memo[r][c]

            memo[r][c] = dfs(r, c + 1) + dfs(r + 1, c)
            
            return memo[r][c]    
        
        return dfs(0, 0)