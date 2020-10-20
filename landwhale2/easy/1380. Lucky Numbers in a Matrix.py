class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row = list(map(min, matrix))
        col = []
        
        for i in range(len(matrix[0])):
            max_ = 0
            for j in range(len(matrix)):
                if max_ < matrix[j][i]:
                    max_ = matrix[j][i]
            col.append(max_)
            
        result = []
        
        for n in row:
            if n in col:
                result.append(n)
        
        
        
        return result
