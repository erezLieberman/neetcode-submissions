class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, current_sum, path):
            if current_sum == target:
                res.append(path[:])
                return
            elif current_sum > target:
                return
            elif i >= len(nums):
                return
            path.append(nums[i])
            backtrack(i, current_sum + nums[i], path)
            path.pop()
            backtrack(i+1, current_sum, path)

        backtrack(0,0,[])
        return res
