class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        wordLen = len(word)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        curPath = []
        def dfs(i, j, wIdx):
            if wIdx >= wordLen:
                return True
            
            # Out of bounds
            pair = (i, j)
            if i < 0 or i >= n or j < 0 or j >= m or pair in curPath:
                return False
            
            curPath.append(pair)

            letter = word[wIdx]
            cell = board[i][j]
            if cell != letter:
                curPath.pop()
                return False
            
            for d in dirs:
                n_i = i + d[0]
                n_j = j + d[1]
                if dfs(n_i, n_j, wIdx + 1):
                    return True
            
            curPath.pop()
            return False
        
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        
        return False