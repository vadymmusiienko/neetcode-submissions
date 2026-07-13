class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        matrix.reverse()

        # Transpose
        for r in range(n - 1):
            for c in range(r + 1, n):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = tmp