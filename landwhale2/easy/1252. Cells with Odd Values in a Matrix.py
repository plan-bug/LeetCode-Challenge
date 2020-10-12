class Solution:
    dy = [0,-1,0,1]
    dx = [-1,0,1,0]
    
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        arr = [[0 for _ in range(m)] for _ in range(n)]
        for y,x in indices:
            arr[y][x] += 2
            for i in range(4):
                ny, nx = y+self.dy[i], x+self.dx[i]
                while 0 <= ny < n and 0 <= nx < m:
                    arr[ny][nx] += 1
                    ny, nx = ny+self.dy[i], nx+self.dx[i]
        result = 0
        
        for i in range(n):
            for j in range(m):
                if not arr[i][j] % 2 == 0:
                    result += 1
        print(arr)
        
        return result
