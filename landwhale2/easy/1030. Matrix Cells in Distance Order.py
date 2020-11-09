class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        arr = []
        for i in range(R):
            for j in range(C):
                arr.append([[i,j],abs(i-r0)+abs(j-c0)])
        arr.sort(key=lambda arr: arr[1])
        return [i[0] for i in arr]
