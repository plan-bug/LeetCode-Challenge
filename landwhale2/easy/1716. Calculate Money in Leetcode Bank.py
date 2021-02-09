class Solution:
    def totalMoney(self, n: int) -> int:
        ro = n // 7
        count, result = 0, 0
        while count <= ro:
            if count == ro:
                for i in range(1, (n%7)+1):
                    result += (i + count)
            else:
                for i in range(1, 8):
                    result += (i + count)
            
            count += 1
            
        
        return result
