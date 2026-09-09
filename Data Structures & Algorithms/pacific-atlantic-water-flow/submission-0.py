class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(row, col, ocean_set, prev_height):
            if (row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in ocean_set or heights[row][col] < prev_height):
                return 
            current_height = heights[row][col]
            ocean_set.add((row, col))
            dfs(row + 1, col, ocean_set, current_height)
            dfs(row - 1, col, ocean_set, current_height)
            dfs(row, col + 1, ocean_set, current_height)
            dfs(row, col - 1, ocean_set, current_height)


        for c in range(COLS):
            dfs(0, c, pacific, 0)
            dfs(ROWS-1, c, atlantic, 0)
            
        for r in range(ROWS):
            dfs(r, 0, pacific, 0)
            dfs(r, COLS-1, atlantic, 0)
                    
        return list(pacific & atlantic)