class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0,0
        target = {}
        current = {}
        min_length = float('inf')
        res = ()
    
        for i in t:
            target[i] = target.get(i, 0) + 1

        need = len(target.keys())
        have = 0

        while r < len(s):
            current[s[r]] = current.get(s[r], 0) + 1
            if current[s[r]] == target.get(s[r]):
                have += 1
            while have == need:
                if r-l+1 < min_length:
                    res = (l, r)
                    min_length = r-l+1
                current[s[l]] = current.get(s[l], 0) - 1
                if s[l] in target and current[s[l]] < target.get(s[l]):
                    have -= 1
                l += 1
            r+=1
            
        if res:
            return s[res[0]:res[1]+1]
        else:
            return ""
             
