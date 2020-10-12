class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        result = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if not abs(arr[i] - arr[j]) <= a:
                        continue
                    if not abs(arr[j] - arr[k]) <= b:
                        continue
                    if not abs(arr[i] - arr[k]) <= c:
                        continue
                    result += 1
        
        return result
                    
