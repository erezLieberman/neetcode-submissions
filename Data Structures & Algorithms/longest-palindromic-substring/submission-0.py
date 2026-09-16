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
            if len(odd_pal) > len(longest):
                longest = odd_pal
            if len(even_pal) > len(longest):
                longest = even_pal 

        return longest