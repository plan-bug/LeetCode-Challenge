class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        count = 0
        for i in s:
            if i == "(":
                count +=1
            if i == ")":
                count -=1
            depth = max(depth, count)
        return depth