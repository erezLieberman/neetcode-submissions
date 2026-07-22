class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for c in s:
            sdict[c] = sdict.get(c, 0) + 1
        for i in t:
            tdict[i] = tdict.get(i, 0) + 1

        if len(s) != len(t):
            return False
        
        return sdict == tdict