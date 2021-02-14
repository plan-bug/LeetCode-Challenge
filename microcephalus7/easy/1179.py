class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alti = 0
        maxAlti = 0
        for i in gain:
            alti+=i
            maxAlti = max(maxAlti,alti)
        return maxAlti