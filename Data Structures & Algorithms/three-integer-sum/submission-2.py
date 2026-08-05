class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        sorted_nums = sorted(nums)
        # print("sorted_nums", sorted_nums)

        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            frozen = sorted_nums[i] * -1
            l = i + 1
            r = len(sorted_nums) - 1
            while l < r:
                if frozen == (sorted_nums[l] + sorted_nums[r]):
                    result.append([frozen * -1, sorted_nums[r], sorted_nums[l]])
                    l+=1
                    r-=1
                    while sorted_nums[r] == sorted_nums[r+1] and l < r:
                        r-=1
                    while sorted_nums[l] == sorted_nums[l-1] and l < r:
                        l += 1
                elif (frozen < sorted_nums[l] + sorted_nums[r]):
                    r -=1
                elif (frozen > sorted_nums[l] + sorted_nums[r]):
                    l += 1   
                     
                 
        return result

        