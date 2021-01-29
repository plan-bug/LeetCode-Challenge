from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


solution = Solution()
print(solution.reverseString(["h", "e", "l", "l", "o"]))
