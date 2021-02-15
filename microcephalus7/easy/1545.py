from itertools import combinations
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        return len([i for i in combinations(arr,3) if abs(i[0]-i[1]) <=a if abs(i[1]-i[2]) <=b if abs(i[0]-i[2]) <=c])
        