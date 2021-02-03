# 그냥 바꿔버려도 된다
# 기존의 데이터로 새로운 데이터를 만들기 보다 기존의 데이터를 수정

class Solution:
    def interpret(self, command: str) -> str:
        
        return command.replace('()','o').replace('(al)','al')
