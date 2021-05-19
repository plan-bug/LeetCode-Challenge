class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        count = 0 
        res = []
        for c in seq:
            if c == "(":
                res.append(count % 2)
                count += 1
            else:
                count -= 1
                res.append(count % 2)                
        return res