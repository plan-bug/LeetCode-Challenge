class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        return sum(sum(v=="X" and (i==0 or board[i-1][j] != "X") and (j==0 or board[i][j-1] != "X") for j, v in enumerate(r)) for i, r in enumerate(board))
