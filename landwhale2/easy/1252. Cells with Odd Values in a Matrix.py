# 처음에는 동서남북 네방향 + 1 씩 올리는 문제인줄알고 풀었었다.
# 실패로 뜨길래 문제 다시 봤더니 해당하는 행, 열 한줄씩 +1 하는 문제였다.
# 코드 다시 고치기 귀찮아서 변형해서 품

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
