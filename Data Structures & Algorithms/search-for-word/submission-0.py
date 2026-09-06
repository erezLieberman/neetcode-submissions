class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(row, col, index):
            if index == len(word):
                return True

            if (row, col) in visited or \
                row < 0 or row >= len(board) or \
                col < 0 or col >= len(board[0]) or \
                board[row][col] != word[index]:
                    return False

            visited.add((row, col))

            if dfs(row+1, col, index+1) or \
               dfs(row-1, col, index+1) or \
               dfs(row, col+1, index+1) or \
               dfs(row, col-1, index+1):
                return True

            visited.remove((row, col))
            return False

        
        for r in range(len(board)):
            for c in range(len(board[0])):
               if dfs(r, c, 0):
                return True

        return False        

        
        
        

