class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
    
        def helper(subnums):
            rob1, rob2 = 0,0
            for num in subnums:
                new_rob = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = new_rob
            return rob2 
        
        return max(helper(nums[:-1]), helper(nums[1:]))