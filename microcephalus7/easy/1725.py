from collections import Counter

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        c= Counter([min(i) for i in rectangles])
        return c[max(c.keys())]