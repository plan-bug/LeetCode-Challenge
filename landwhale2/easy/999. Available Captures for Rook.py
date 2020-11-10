class Solution:
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'R':
                    answer = self.go(j,i, board)
        return answer
    
    def go(self,x,y, board):
        answer = 0
        for i in range(4):
            nx = x + self.dx[i]
            ny = y + self.dy[i]
            while True:
                if 0 <= nx < len(board[0]) and 0 <= ny < len(board):
                    if board[ny][nx].isupper():
                        break
                    elif board[ny][nx].islower():
                        answer += 1
                        break
                    else:
                        nx = nx + self.dx[i]
                        ny = ny + self.dy[i]
                        continue
                else:
                    break
                    
        return answer
