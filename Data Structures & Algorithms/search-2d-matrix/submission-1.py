class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return -1
        
        row_len = len(matrix[0])

        # Find row
        left = 0
        right = len(matrix) - 1
        row_idx = -1
        while left <= right:
            mid = left + ((right - left) // 2)
            lower = matrix[mid][0]
            upper = matrix[mid][row_len - 1]

            if target < lower:
                right = mid -1
            elif target > upper:
                left = mid + 1
            else:
                row_idx = mid
                break
        
        if row_idx == -1:
            return False
        
        # Find elem
        left = 0
        right = row_len - 1
        while left <= right:
            mid = left + ((right - left) // 2)

            if target < matrix[row_idx][mid]:
                right = mid - 1
            elif target > matrix[row_idx][mid]:
                left = mid + 1
            else:
                return True
        
        return False

        

            