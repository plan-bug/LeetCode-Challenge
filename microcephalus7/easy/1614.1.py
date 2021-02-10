class Solution:
    def maxDepth(self, s: str) -> int:
        return max(accumulate(filter(None, map({"(":1,")":-1}.get,s))),default=0)