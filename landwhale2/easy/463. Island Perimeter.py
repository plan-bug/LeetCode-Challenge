class Solution:
    xi = [0,1,0,-1]
    xj = [1,0,-1,0]
    def finder(self, i,j, grid):
        count = 0
        for k in range(4):
            ni = i + self.xi[k]
            nj = j + self.xj[k]

            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                if grid[ni][nj] == 1:
                    count += 1
        
        return count
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = self.finder(i, j, grid)
                    result[i][j] = 4 - count

        answer = 0
        for i in range(len(result)):
            for j in range(len(result[0])):
                answer += result[i][j]

        return answer
