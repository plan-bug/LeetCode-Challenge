# for 문 사용
# 쌓이는 돈 변수 생성
# 5달러를 기준으로 차액 생성
# 쌓이는 돈 차액으로 뺌
# 쌓이는 돈 음수값 될 시 False
# 쌓이는 돈 양수값 일 시 True
# 5달러


from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        rest = 0
        for i in bills:
            if i == 5:
                rest += i
            else:
                rest -= (i-5)
                if rest < 0:
                    return False
                rest += i
        return rest


solution = Solution()
print(solution.lemonadeChange([5, 5, 5, 10, 20]))
print(solution.lemonadeChange([5, 5, 10]))
print(solution.lemonadeChange([10, 10]))
print(solution.lemonadeChange([5, 5, 10, ]))
print(solution.lemonadeChange([5, 10, 5, 20]))
