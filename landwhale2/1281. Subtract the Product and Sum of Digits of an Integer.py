class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(map(int , str(n)))
        result = n[0]
        for i in n[1:]:
            result *= i
        return result - sum(n)
            
