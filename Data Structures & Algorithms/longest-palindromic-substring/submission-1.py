class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        def helper(l, r):
            while l>=0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]
            
        
        for i in range(len(s)):
            odd_pal = helper(i, i)
            even_pal = helper(i, i+1)
            longest = max(longest, odd_pal, even_pal, key=len)

        return longest