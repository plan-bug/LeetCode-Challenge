# 5, 10 달러 변수로 둠
# for 문으로 bills 돌림
# i 와 5,10 의 상황에 따라 if 문으로 분기
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if five <= 0:
                    return False
                five -= 1
                ten += 1
            else:
                if ten > 0 and five > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
