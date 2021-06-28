class Solution:
    def minFlips(self, target: str) -> int:
        res = 0
        status = "0"

        for i in target:
            if i != status:
                res += 1
                status = i
        return res
