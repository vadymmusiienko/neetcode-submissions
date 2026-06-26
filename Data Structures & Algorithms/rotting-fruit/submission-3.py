from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        fresh_n = 0
        rotten_coords = []

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_n += 1
                elif grid[r][c] == 2:
                    rotten_coords.append((r, c))

        queue = deque(rotten_coords)
        minute = 0

        while queue and fresh_n > 0:

            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh_n -= 1
                        queue.append((nr, nc))

            minute += 1

        return minute if fresh_n == 0 else -1