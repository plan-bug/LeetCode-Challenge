class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        l = 0
        result = 0
        for st in s:
            if st == 'R':
                r += 1
            else:
                l += 1
            if r > 0 and l > 0:
                if r == l:
                    result += 1
                    r, l = 0,0
        return result
