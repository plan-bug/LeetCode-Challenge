class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        if len(mat) == 1:
            return mat[0][0]
        
        for i in range(len(mat)):
            result += mat[i][i]
            mat[i][i] = 0
        

        for i in range(len(mat)):
            result += mat[i][len(mat)-1-i]
            mat[i][len(mat)-1-i] = 0
            
        return result
