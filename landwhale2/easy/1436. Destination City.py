class Solution:
    def bfs(self,arr):
        q = [arr[0][0]]
        visited = []
        while q:
            node = q.pop(0)
            for i in range(len(arr)):
                if arr[i][0] == node and arr[i][0] not in visited:
                    visited.append(arr[i][0])
                    q.append(arr[i][1])
                    last = arr[i][1]
                    break
        return last
        
    
    def destCity(self, paths: List[List[str]]) -> str:
        return self.bfs(paths)
