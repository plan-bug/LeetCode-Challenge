class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        out = []
        def backTrack(path,nextpos):
            if path[-1] == len(graph) -1 :
                out.append(path)
                return
            for i in nextpos:
                backTrack(path +[i],graph[i])
        for start in graph[0]:
            backTrack([0,start],graph[start])
        return out