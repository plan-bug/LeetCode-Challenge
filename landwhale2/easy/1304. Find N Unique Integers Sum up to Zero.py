class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n == 1:
            return [0]
        
        if n % 2 == 0:
            for i in range(2, n+2):
                if i % 2 == 0:
                    result.append(i//2)
                else:
                    result.append(-(i//2))
        else:
            for i in range(2, n+1):
                if i % 2 == 0:
                    result.append(i//2)
                else:
                    result.append(-(i//2))
            result.append(0)
        

        
        return result
