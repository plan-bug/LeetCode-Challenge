class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        result = 0
        for j in range(len(A[0])):
            tmp = ''
            for i in range(len(A)):
                tmp += A[i][j]
            if tmp != ''.join(sorted(tmp)):
                result += 1
        
        return result
