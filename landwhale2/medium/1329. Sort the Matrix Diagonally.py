class Solution:
    def find_val(self, i, j, mat):
        values = []
        ti, tj = i, j
        while True:
            print(ti, tj)
            value = mat[ti][tj]
            values.append(value)
            ti += 1
            tj += 1
            if 0 <= ti < len(mat) and 0 <= tj < len(mat[ti]):
                pass
            else:
                break
        
        values = sorted(values)
        return values
    
    def set_val(self, i, j, values, mat):
        index = 0
        while index < len(values):
            mat[i][j] = values[index]
            i += 1
            j += 1
            index += 1
        
    
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for i in range(len(mat)-1, -1, -1):
            values = self.find_val(i, 0, mat)
            self.set_val(i,0, values, mat)
            
            if i == 0:
                for j in range(1, len(mat[i])):
                    values = self.find_val(i, j, mat)
                    self.set_val(i,j, values, mat)
        
        return mat
