class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        nums_length = len(nums)
        suffix = [1 for i in nums]
        

        for i in range(1,nums_length):
            prefix.append(nums[i-1] * prefix[i-1])
        
        for i in range(nums_length-2,-1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        result = []

        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        return result

                
        