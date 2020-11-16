from collections import Counter
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        set_A = set(A[0])
        for a in A[1:]:
            set_A = set_A.intersection(a)
        common_letters = []
        for letter in set_A:
            count = 101
            for a in A:
                count = min(count, a.count(letter))
            common_letters += [letter] * count
        return common_letters


solution = Solution()
print(solution.commonChars(["bella", "label", "roller"]))
