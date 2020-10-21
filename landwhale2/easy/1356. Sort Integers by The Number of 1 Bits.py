class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return [x for x,y in sorted([[n, bin(n)[2:].count('1')] for n in arr], key=lambda x:(x[1], x[0]))]
        
