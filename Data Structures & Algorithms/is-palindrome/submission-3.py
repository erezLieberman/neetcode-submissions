class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        if not s:
            return True

        while l < r:
            if not s[l].isalnum():
                l +=1
            if not s[r].isalnum():
                r-=1
            elif s[l].isalnum() and s[r].isalnum():
                if s[l].lower() == s[r].lower():
                    l +=1
                    r -= 1
                else:
                    print("s[l]", s[l])
                    print("s[r]", s[r])
                    return False
     
        return True