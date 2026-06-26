from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return grid

        n = len(grid) # Rows
        m = len(grid[0]) # Cols
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Find coords of the chest
        chests_coords = [] # [(ridx, cidx),...]
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    chests_coords.append((r, c))
        
        # Run BFS for every chest
        for chest_ridx, chest_cidx in chests_coords:

            queue = deque([(chest_ridx, chest_cidx)])
            seen = set()
            level = 0

            while queue:
                for _ in range(len(queue)):
                    ridx, cidx = queue.popleft()
                    
                    if (ridx, cidx) in seen:
                        continue

                    seen.add((ridx, cidx))
                    if grid[ridx][cidx] == -1:
                        continue

                    grid[ridx][cidx] = min(level, grid[ridx][cidx])
                    
                    # Append neighbors
                    for inc_r, inc_c in directions:
                        new_r = ridx + inc_r
                        new_c = cidx + inc_c
                        
                        if new_r < n and new_r >= 0 and new_c < m and new_c >= 0:
                            queue.append((new_r, new_c))
                
                level += 1
