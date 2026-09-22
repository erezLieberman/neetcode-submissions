class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min, global_max = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            temp_cur_max = cur_max
            cur_max = max(num * cur_max, num * cur_min, num)
            cur_min = min(num * temp_cur_max, num * cur_min, num)
            global_max = max(global_max, cur_max)
            # print("cur_max", cur_max)
            # print("cur_min", cur_min)
            # print("global_max", global_max)
        
        return global_max
