class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro = 1
        sum = 0
        
        for i in str(n):
            pro *=int(i)
            sum +=int(i)
        return pro -sum