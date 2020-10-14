class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right+1):
            if len(str(i)) > 1:
                check = True
                for j in str(i):
                    if j == '0' or not i % int(j) == 0:
                        check = False
                        break
                if check:
                    result.append(i)
            else:
                result.append(i)
        
        return result
