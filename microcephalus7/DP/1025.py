# init 시 딕셔너리 생성
# 해당 딕셔너리엔 숫자에 대한 true/false 저장
# 재귀함수로 return 값 이용

class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0
