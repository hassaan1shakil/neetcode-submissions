class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        low = 0
        high = len(matrix) - 1
        
        while low <= high:
            mid = low + (high - low) // 2

            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                return True
        
        row = high
        low = 0
        high = len(matrix[0]) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if matrix[row][mid] > target:
                high = mid - 1
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                return True

        return False
