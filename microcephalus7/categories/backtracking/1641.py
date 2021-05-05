# 알고리즘 주제가 정해져있다고 해서 그 방법에 한정될 필요는 없음
# 조합으로 풀 수도 있음

import itertools
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return len(list(itertools.combinations_with_replacement(range(5),n)))
