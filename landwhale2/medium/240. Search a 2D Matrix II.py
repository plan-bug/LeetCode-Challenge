class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        column = len(matrix[0])-1
    
        while 0 <= row < len(matrix) and 0 <= column < len(matrix[0]):
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                row += 1
            else:
                column -= 1
        return False
