class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        result = True
        arr = sorted(arr)
        gap = abs(arr[1]-arr[0])
        
        for i in range(len(arr)-1):
            if abs(arr[i+1] - arr[i]) != gap:
                result = False
                break
        
        return result
