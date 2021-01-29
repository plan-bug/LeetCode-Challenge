# J,S 둘다 list 형성
# count 변수 생성
# J 이터레이션
# lambda 식으로 S 돌며 j와 같은 list 만든 뒤 길이 만큼 count 올림

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J, S = list(J), list(S)
        count = 0
        for j in J:
            if j in S:
                count += len(list(map(lambda i: i == j, S)))
        return count


solution = Solution()
print(solution.numJewelsInStones("jJ", "jJJ"))
