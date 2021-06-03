class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (
                    board[i][j] == "X"
                    and (i == 0 or board[i - 1][j] != "X")
                    and (j == 0 or board[i][j - 1] != "X")
                ):
                    count += 1
        return count
