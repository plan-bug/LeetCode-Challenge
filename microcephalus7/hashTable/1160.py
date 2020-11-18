# words 엘리먼트로 Counter 생성
# words 엘리먼트를 chars 를 Counter 한 거 뺌
# 뺀 게 빈 Counter 일 경우 words 를 arr 에 더 함
# arr의 길이를 더 한 수 return

from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum([len(w) for w in words if not (Counter(w) - Counter(chars))])


solution = Solution()
print(solution.countCharacters(["cat", "bt", "hat", "tree"], "atach"))
