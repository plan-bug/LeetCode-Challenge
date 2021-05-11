# edges 에서 2번째 요소만 추출
# 모여진 요소 counter 로 dict
# dict 에서 가장 작은 빈도 찾기
# 작은 빈도와 일치하는 key list 에 삽입
# list return 
from collections import defaultdict

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return list(set(range(n)) - set(i[1] for i in edges))
