class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        wordLen = len(word)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i, j, wIdx):
            if wIdx >= wordLen:
                return True
            
            # Out of bounds or in seen
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] == "#" or board[i][j] != word[wIdx]:
                return False
            
            # Visited in place
            tmp = board[i][j]
            board[i][j] = "#"
            
            for d in dirs:
                n_i = i + d[0]
                n_j = j + d[1]
                if dfs(n_i, n_j, wIdx + 1):
                    return True
            
            board[i][j] = tmp
            return False
        
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        
        return False