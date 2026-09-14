class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(step, memo):
            if step == 1:
                return 1
            if step == 2:
                return 2
            if step in memo:
                return memo[step]
            else:
                memo[step] = dfs(step-1, memo) + dfs(step-2, memo)
                return memo[step]
        
        memo = {}
        return dfs(n, memo)

        
