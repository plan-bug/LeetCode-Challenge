# string 각 각각 list 로 변경
# 정렬 한 후 값 같으면 True 아니면 False

from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t)) and True or False


solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("cat", "dog"))
print(solution.isAnagram("a", "ab"))
