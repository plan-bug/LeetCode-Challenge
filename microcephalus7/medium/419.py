# 다시 봐야함
# 이터레이터
# 원리
# 중복되는 것을 거르기
# 배열에서 이웃하는 것들 중에서도 그 차이점


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        return sum(
            sum(
                board[i][j] == "X"
                and (i == 0 or board[i - 1][j] != "X")
                and (j == 0 or board[i][j - 1] != "X")
                for j in range(len(board[i]))
            )
            for i in range(len(board))
        )
