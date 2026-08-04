class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_length = 0

        for num in hashset:
            if num -1 in hashset:
                continue
            else:
                start = num
            length = 1
            while start +1 in hashset:
                start += 1
                length += 1
            if length > max_length:
                max_length = length
        return max_length

            