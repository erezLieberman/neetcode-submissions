class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        one_step_back = max(nums[0], nums[1])
        two_steps_back = nums[0]

        for i in range(2,len(nums)):
            current = max(nums[i] + two_steps_back, one_step_back)
            print("current",current)
            two_steps_back = one_step_back
            print("two_steps_back",two_steps_back)
            one_step_back = current
            print("one_step_back",one_step_back)
            
        
        return max(two_steps_back, one_step_back)
            