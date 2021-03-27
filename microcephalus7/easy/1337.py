class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [r[1] for r in heapq.nsmallest(k,[[sum(g),i] for i,g in enumerate(mat)])]