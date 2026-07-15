class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        if n == 1:
            return matrix[0]
        if m == 1:
            return [n[0] for n in matrix]

        topLeft = (0, 0)
        bottomRight = (n - 1, m - 1)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []

        def legal(r, c, tL, bR):
            if r == tL[0] and c == tL[1]:
                return False

            if r < tL[0] or r > bR[0]:
                return False
            
            if c < tL[1] or c > bR[1]:
                return False
            
            return True
            

        # for level in range((min(n, m) + 1) // 2):
        while topLeft[0] <= bottomRight[0] and topLeft[1] <= bottomRight[1]:
            # One row left
            if topLeft[0] == bottomRight[0]:
                for c in range(topLeft[1], bottomRight[1] + 1):
                    res.append(matrix[topLeft[0]][c])
                break

            # One column left
            if topLeft[1] == bottomRight[1]:
                for r in range(topLeft[0], bottomRight[0] + 1):
                    res.append(matrix[r][topLeft[1]])
                break

            curR, curC = topLeft
            res.append(matrix[curR][curC])

            # Right, down, left, up
            for d in dirs:
                while legal(curR + d[0], curC + d[1], topLeft, bottomRight):
                    curR, curC = curR + d[0], curC + d[1]
                    res.append(matrix[curR][curC])

            # Update level boundaries
            topLeft = (topLeft[0] + 1, topLeft[1] + 1)
            bottomRight = (bottomRight[0] - 1, bottomRight[1] - 1)
        
        return res