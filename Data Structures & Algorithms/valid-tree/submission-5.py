class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        
        adjacency_map = {i:[] for i in range(n)}

        for k, v in edges:
          adjacency_map[k].append(v)
          adjacency_map[v].append(k)

        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbor in adjacency_map[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                if neighbor not in visited:
                    if not dfs(neighbor, node):
                        return False
            return True
           
        return dfs(0, -1) and len(visited) == n
