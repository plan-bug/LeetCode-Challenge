class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        return [*{*map(min, matrix)} & {*map(max,zip(*matrix))}]