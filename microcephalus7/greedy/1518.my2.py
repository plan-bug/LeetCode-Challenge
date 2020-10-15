# while 문의 조건식 변경
# 나눔의 몫이 있다는 건 크거나 같다는 것.

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        while numBottles >= numExchange:
            newBottle = numBottles // numExchange
            drank += newBottle
            numBottles = newBottle+(numBottles % numExchange)
        return drank
