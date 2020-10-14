# balance 개념 (플러스 마이너스가 0이 된다)
# L,R 이 number 값을 +1, -1 함
# number 값이 0 이 될 때마다 string 수를 +1 씩 함.
# string 값 return

# 법칙 살펴보기

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        number = 0
        string = 0
        for i in s:
            if i == 'L':
                number += 1
            else:
                number -= 1
            if number == 0:
                string += 1
        return string


solution = Solution()
print(solution.balancedStringSplit("LRLR"))
