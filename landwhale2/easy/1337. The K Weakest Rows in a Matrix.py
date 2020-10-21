class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [x for x,y in sorted([[i, sum(mat[i])] for i in range(len(mat))], key=lambda x:x[1])][:k]
