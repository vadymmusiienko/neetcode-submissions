class Solution:
    def solve(self, board: List[List[str]]) -> None:
        safe = set()
        ROWS, COLS = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, safe):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return

            coord = (r, c)
            val = board[r][c]
            if coord in safe or val == 'X':
                return
            safe.add(coord)

            for d in dirs:
                new_r, new_c = r + d[0], c + d[1]
                dfs(new_r, new_c, safe)

        # Find all safe
        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c, safe)
            if board[ROWS - 1][c] == 'O':
                dfs(ROWS - 1, c, safe)
        
        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r, 0, safe)
            if board[r][COLS - 1] == 'O':
                dfs(r, COLS - 1, safe)
        
        # Flip unsafe
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r, c) not in safe:
                    board[r][c] = 'X'
