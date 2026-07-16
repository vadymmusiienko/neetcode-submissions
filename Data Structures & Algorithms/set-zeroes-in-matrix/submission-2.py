class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        firstRowZero = False
        firstColZero = False
        
        def zeroRow(rIdx):
            for i in range(m):
                matrix[rIdx][i] = 0
        
        def zeroCol(cIdx):
            for i in range(n):
                matrix[i][cIdx] = 0

        # Top row and left column are tracking zero rows and cols
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:

                    if i == 0:
                        firstRowZero = True
                    
                    if j == 0:
                        firstColZero = True

                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, n):
            if matrix[i][0] == 0:
                zeroRow(i)
        
        for j in range(1, m):
            if matrix[0][j] == 0:
                zeroCol(j)
        
        if firstColZero:
            zeroCol(0)
        if firstRowZero:
            zeroRow(0)

        