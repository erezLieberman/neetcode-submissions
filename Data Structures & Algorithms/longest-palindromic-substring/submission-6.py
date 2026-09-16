class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        start_index = 0

        def helper(l, r):
            while l>=0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return r-l-1
            
        
        for i in range(len(s)):
            odd_pal = helper(i, i)
            even_pal = helper(i, i+1)
            if odd_pal > max_length:
                start_index = i - (odd_pal // 2)
            if even_pal > max_length:
                start_index = i+1 - (even_pal // 2)
            max_length = max(max_length, odd_pal, even_pal)

        return s[start_index:start_index + max_length]