class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for s in A:
            if s % 2 == 0:
                even.append(s)
            else:
                odd.append(s)
        
        return sorted(even) + sorted(odd)
