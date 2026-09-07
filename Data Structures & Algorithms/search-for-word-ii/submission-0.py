class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            node = root
            for c in word:
                if not c in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word

        visited = set()
        results = []

        def dfs(r, c, node):
            if r < 0 \
            or r >= len(board) \
            or c < 0 \
            or c >= len(board[0]) \
            or (r, c) in visited:
                return

            char = board[r][c]

            if char not in node.children:
                return
            else:
                next_node = node.children[char]
                if next_node.word:
                    results.append(next_node.word)
                    next_node.word = None
                visited.add((r, c))
                dfs(r+1, c, next_node)
                dfs(r-1, c, next_node)
                dfs(r, c+1, next_node)
                dfs(r, c-1, next_node)
                visited.remove((r, c))

            return

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root)

        return results

        