class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = str(x)[1:]
            x = x[::-1]
            x = "-" + x
            x = int(x)
        else:
            x = int(str(x)[::-1])
        
        if(x<pow(-2,31) or x>=pow(2,31)):
            return 0
        
        return x
