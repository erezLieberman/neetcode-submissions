class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        memo = {}

        def dfs(i, memo):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            print("i", i)
            print("len(nums)-1", len(nums)-1)
            print("nums[i]", nums[i])
            memo[i] = max(dfs(i-1, memo), nums[i] + dfs(i-2, memo))
            return memo[i]
        
        return dfs(len(nums)-1, memo)
            