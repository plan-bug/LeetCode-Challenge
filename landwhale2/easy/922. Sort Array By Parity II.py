class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        result = []
        for n in A:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
        
        for o,e in zip(odd, even):
            result.extend([e,o])
        
        return result
