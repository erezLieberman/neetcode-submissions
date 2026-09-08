"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        original_to_cloned = {}

        def dfs(node):
            if node not in original_to_cloned:
                clone = Node(node.val)
                original_to_cloned[node] = clone
                for neighbor in node.neighbors: 
                    clone.neighbors.append(dfs(neighbor))
                return clone
            return original_to_cloned[node]

        return dfs(node)
