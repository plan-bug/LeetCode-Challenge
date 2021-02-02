class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = [0]
        
        for g in gain:
            result.append(result[-1] + g)
        
        return max(result)
