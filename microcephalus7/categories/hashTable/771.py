
# list 된 J 이터레이션
# S안에서 j 갯수 요소 가진 리스트 생성
# list 합계 return
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(map(lambda j: S.count(j), list(J)))
