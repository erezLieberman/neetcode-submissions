class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        memo = [nums[0], max(nums[0], nums[1])]

        for i in range(2,len(nums)):
            memo.append(max(memo[i-1], memo[i-2] + nums[i]))
        
        return max(memo)
            