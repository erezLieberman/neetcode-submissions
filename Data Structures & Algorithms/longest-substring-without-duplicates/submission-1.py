class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l, r = 0,0
        max_length = 0

        while r < len(s):
            if s[r] in hashset:
                hashset.remove(s[l])
                l+=1
            else:
                hashset.add(s[r])
                r+=1
            max_length = max(max_length, r-l)
        return max_length
