from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacencies_map = defaultdict(list)
        res = 0

        for k,v in edges:
            adjacencies_map[k].append(v)
            adjacencies_map[v].append(k)

        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in adjacencies_map[node]:
                if neighbor not in visited:
                    dfs(neighbor)


        for i in range(n):
            if i not in visited:
                res += 1
                visited.add(i)
                dfs(i)

        return res
