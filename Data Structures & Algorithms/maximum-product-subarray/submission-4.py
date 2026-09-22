class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min, global_max = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            cur_max, cur_min = max(num * cur_max, num * cur_min, num), min(num * cur_max, num * cur_min, num)
            global_max = max(global_max, cur_max)
        
        return global_max
