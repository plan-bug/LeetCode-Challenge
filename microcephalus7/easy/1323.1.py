# 논리에 맞는 메소드를 찾는 것도 능력
class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6','9',1))
