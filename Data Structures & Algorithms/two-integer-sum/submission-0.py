class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            diffrence = target - nums[i]
            if diffrence in hashmap:
                return [hashmap[diffrence],i]
            else:
                hashmap[nums[i]] = i