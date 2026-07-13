class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Transpose
        for r in range(n - 1):
            for c in range(r + 1, n):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = tmp
        
        # Mirror y-axis
        for r in range(n):
            for c in range(n // 2):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[r][n - 1 - c]
                matrix[r][n - 1 - c] = tmp
        
        




