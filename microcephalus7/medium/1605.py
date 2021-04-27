class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        res = [[0 for j in range(len(colSum))] for i in range(len(rowSum))]
        i = 0
        j = 0
        while i <len(rowSum) and j<len(colSum):
            res[i][j] = min(rowSum[i],colSum[j])
            if rowSum[i] == colSum[j]:
                i += 1
                j+=1
            elif rowSum[i] > colSum[j]:
                rowSum[i]-=colSum[j]
                j+=1
            else:
                colSum[j] -= rowSum[i]
                i += 1
        return res