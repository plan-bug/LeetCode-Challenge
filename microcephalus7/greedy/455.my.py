# 그리디 기준은 사람
# 포인터는 2개 둠
# g[i] 보다 s[i] 가 큰 경우 (쿠키를 줄 수 있는 경우)와 아닌 경우로 나눔
# g 의 [i] 값 return

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gPoint, sPoint = 0, 0
        while gPoint < len(g) and sPoint < len(s):
            if g[gPoint] <= s[sPoint]:
                gPoint += 1
                sPoint += 1
            else:
                sPoint += 1
        return gPoint


solution = Solution()
print(solution.findContentChildren([1, 2, 3], [1, 1]))
print(solution.findContentChildren([1, 2, 3], [1, 2]))
