class Solution:
    def __init__(self) -> None:
        self.memo={}
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.memo = {len(graph)-1:[[len(graph)-1]]}
        def calc(N):
            if N in self.memo:
                return self.memo[N]
            a = []
            for n in graph[N]:
                for path in calc(n):
                    a.append([N]+path)
            self.memo[N]=a
            return a
        return calc(0)