class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return -1
        
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = n * m - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            row_idx = mid // m
            col_idx = mid % m
            elem = matrix[row_idx][col_idx]

            if target > elem:
                left = mid + 1
            elif target < elem:
                right = mid - 1
            else:
                return True
        
        return False
