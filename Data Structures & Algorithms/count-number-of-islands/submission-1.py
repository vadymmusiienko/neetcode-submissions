class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        n = len(grid) # Num of rows
        m = len(grid[0]) # Num of cols
        islands = 0
        visited = set()

        def explore(start):
            if start in visited:
                return

            visited.add(start)

            if grid[start[0]][start[1]] == "0":
                return

            # left
            if start[1] > 0:
                explore((start[0], start[1] - 1))

            # right
            if start[1] < m - 1:
                explore((start[0], start[1] + 1))

            # up
            if start[0] > 0:
                explore((start[0] - 1, start[1]))

            # down
            if start[0] < n - 1:
                explore((start[0] + 1, start[1]))

        curr = (0, 0)
        while curr[0] < n:
            val = grid[curr[0]][curr[1]]

            if curr not in visited and val == "1":
                islands += 1
                explore(curr)


            curr = (curr[0] + ((curr[1] + 1) // m), (curr[1] + 1) % m)
        
        return islands
