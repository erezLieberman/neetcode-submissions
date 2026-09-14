from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict()

        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True
            visit[c] = False
            res.append(c)
            return False
                

        for word in words:
            for c in word:
                if c not in adj:
                    adj[c] = set()

        for i in range(1,len(words)):
            if len(words[i-1]) > len(words[i]) and words[i-1].startswith(words[i]):
                    return ""
            for j in range(min(len(words[i-1]), len(words[i]))):
                if words[i-1][j] != words[i][j]:
                    adj[words[i-1][j]].add(words[i][j])
                    break
        
        visit = {}
        res = []

        for k in adj.keys():
            if dfs(k):
                return ""

        return "".join(res[::-1])

        

        


