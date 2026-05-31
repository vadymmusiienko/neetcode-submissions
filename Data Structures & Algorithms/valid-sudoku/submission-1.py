class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        SIZE = 9

        rows = [0] * SIZE
        columns = [0] * SIZE
        squares = [0] * SIZE

        for i in range(SIZE):
            for j in range(SIZE):
                curr_cell = board[i][j]
                if curr_cell == ".":
                    continue

                cell_val = int(curr_cell) - 1 # Because 1-9 and we need 0 - 8
                mask = (1 << cell_val)

                # rows
                if mask & rows[i]:
                    return False
                rows[i] = rows[i] | mask
                
                # cols
                if mask & columns[j]:
                    return False
                columns[j] = columns[j] | mask

                # squares
                square_idx = ((i // 3) * 3) + (j // 3)
                if mask & squares[square_idx]:
                    return False
                squares[square_idx] = squares[square_idx] | mask
        
        return True

                
        