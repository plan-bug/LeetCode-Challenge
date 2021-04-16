class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        M,N,D = len(mat), len(mat[0]),defaultdict(list)
        for i,j in itertools.product(range(M),range(N)):
            D[i-j].append(mat[i][j])
        for k in D:
            D[k].sort(reverse = True)
        return [[D[i-j].pop() for j in range(N)]for i in range(M)]