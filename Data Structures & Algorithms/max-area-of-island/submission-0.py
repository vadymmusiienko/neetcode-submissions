class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        n = len(grid) # Rows
        m = len(grid[0]) # Cols

        max_area = 0
        cur_area = 0
        seen = set()

        # Left, Right, Up, Down
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def visit_island(ridx, cidx):
            nonlocal cur_area

            # Out of bounds check + water + seen
            if ridx < 0 or ridx >= n or cidx < 0 or cidx >= m or not grid[ridx][cidx] or (ridx, cidx) in seen:
                return

            seen.add((ridx, cidx))
            cur_area += 1
            for ri, ci in directions:
                visit_island(ridx + ri, cidx + ci)
        
        for r in range(n):
            for c in range(m):

                # Water + seen 
                if (r, c) in seen or not grid[r][c]:
                    continue
                
                # Find cur islands area
                visit_island(r, c)
                max_area = max(max_area, cur_area)
                cur_area = 0
        
        return max_area

                

        