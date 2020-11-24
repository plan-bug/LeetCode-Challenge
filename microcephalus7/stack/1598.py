# number = 0 둠
# logs 이터레이션
# i에 따라 number +/-
# return number

from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        counter = 0
        for i in logs:
            url = i[:-1]
            if url == '.':
                continue
            elif url == '..':
                if counter == 0:
                    continue
                counter -= 1
            else:
                counter += 1
        return counter


solution = Solution()
print(solution.minOperations(["d1/", "d2/", "../", "d21/", "./"]))
