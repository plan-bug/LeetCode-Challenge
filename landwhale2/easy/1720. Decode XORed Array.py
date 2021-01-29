class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in encoded:
            res.append(res[-1]^i)
        
        return res
