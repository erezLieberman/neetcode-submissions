class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0

        def is_palindrom(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                nonlocal counter
                counter +=1
                right += 1
                left -= 1


        for i in range(len(s)):
            is_palindrom(i, i)
            is_palindrom(i, i+1)
        return counter

        