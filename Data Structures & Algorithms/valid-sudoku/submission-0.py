class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        SIZE = 9

        squares = [set() for _ in range(SIZE)]
        rows = [set() for _ in range(SIZE)]
        columns = [set() for _ in range(SIZE)]

        for i in range(SIZE):
            for j in range(SIZE):
                curr_cell = board[i][j]
                if curr_cell == ".":
                    continue

                # rows
                if curr_cell in rows[i]:
                    return False
                rows[i].add(curr_cell)
                
                # cols
                if curr_cell in columns[j]:
                    return False
                columns[j].add(curr_cell)

                # squares
                square_idx = (math.floor(i / 3) * 3) + math.floor(j / 3)
                if curr_cell in squares[square_idx]:
                    print("SQQQQ")
                    return False
                squares[square_idx].add(curr_cell)
        
        return True

                
        