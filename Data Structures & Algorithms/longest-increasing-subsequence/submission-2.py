class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def recursive(index, previous_included_number):
            if index == len(nums):
                return 0
            state = (index, previous_included_number) 
            if state in memo:
                return memo[state]
            if nums[index] > previous_included_number:
                score = max(recursive(index+1, previous_included_number), 1 + recursive(index+1, nums[index]))
            else:
                score = recursive(index+1, previous_included_number)
            memo[state] = score
            return memo[state]
        return recursive(0, float("-inf"))