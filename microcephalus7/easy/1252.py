class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        res = [[0 for i in range(m)] for j in range(n)]
        def inc(x,y):
            for i in range(m):
                res[x][i] += 1
            for i in range(n):
                res[i][y] +=1
        for i in indices:
            inc(i[0], i[1])
        return sum([0 if n %2 == 0 else 1 for l in res for n in l])