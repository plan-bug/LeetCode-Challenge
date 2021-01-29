# while 문
# numbottles 를 numExchange 값으로 나누고 몫과 나머지를 이용

# 매 순간 최선의 선택 (나눈 값과 남은 값을 더함)


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        while numBottles // numExchange != 0:
            newBottle = numBottles // numExchange
            drank += newBottle
            numBottles = newBottle+(numBottles % numExchange)
        return drank
