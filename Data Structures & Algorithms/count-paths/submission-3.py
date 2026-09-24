class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        if m ==1 and n ==1:
            return 1
        def dfs(r, c):
            if r == 0 and c == 0:
                return 
            if r == 0 or c == 0:
                return 1
            path = (r, c)
            if path in memo:
                return memo[path]
            else:
                memo[path] = dfs(r-1, c) + dfs(r, c-1)
            return memo[path]
        return dfs(m-1, n-1)    