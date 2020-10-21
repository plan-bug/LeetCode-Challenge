from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = []
        for i in range(len(A[0])):
            check = True
            for j in range(1, len(A)):
                if A[0][i] not in A[j]:
                    check = False
                    break
            
            if check:
                for j in range(1, len(A)):
                    A[j] = A[j].replace(A[0][i], '', 1)
                result.append(A[0][i])
        
        return result
