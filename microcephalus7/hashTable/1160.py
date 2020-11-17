# words 엘리먼트로 Counter 생성
# 엘리먼트의 인덱스 값과 chars 의 index 값 이터레이션 하며 크기 비교
# 모든 요소가 chars Counter 보다 작을 때 list 삽입

from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        wordsCounter = [Counter(i) for i in words]
        charsCounter = Counter(chars)
        arr = []
        for i in range(len(words)):
            charsMinus = (wordsCounter[i]-charsCounter)
            charsMinus == Counter() and arr.append(words[i]) or None
        return sum([len(i)for i in arr])


solution = Solution()
print(solution.countCharacters(["cat", "bt", "hat", "tree"], "atach"))
