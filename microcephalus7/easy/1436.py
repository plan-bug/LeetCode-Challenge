class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return [i[1] for i in paths if i[1] not in [j[0] for j in paths]][0]