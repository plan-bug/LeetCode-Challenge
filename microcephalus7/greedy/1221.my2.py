# L 과 R 값이 같아질 때 string 1 씩 더함

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L = 0
        R = 0
        string = 0
        for i in s:
            if i == 'L':
                L += 1
            else:
                R += 1
            if L == R:
                string += 1
        return string


solution = Solution()
print(solution.balancedStringSplit("LRLR"))
