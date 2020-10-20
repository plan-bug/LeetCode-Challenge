class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        target = sorted(heights)
        result = 0
        for i in range(len(heights)):
            if target[i] != heights[i]:
                result += 1
        
        return result
