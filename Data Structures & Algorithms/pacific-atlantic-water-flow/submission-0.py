class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, ocean):
            coord = (r, c)
            if coord in ocean:
                return

            ocean.add(coord)
            height = heights[r][c]

            for d in dirs:
                new_r, new_c = r + d[0], c + d[1]

                if 0 <= new_r < ROWS and 0 <= new_c < COLS and heights[new_r][new_c] >= height:
                    dfs(new_r, new_c, ocean)


            
        
        # Pacific
        pacific = set()
        for c in range(COLS):
            dfs(0, c, pacific)
        
        for r in range(1, ROWS):
            dfs(r, 0, pacific)
        
        # Atlantic
        atlantic = set()
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic)
        
        for r in range(ROWS - 1):
            dfs(r, COLS - 1, atlantic)
        
        return [[r, c] for r, c in pacific & atlantic]

