class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)-1):
            result.append(max(arr[i+1:]))
        return result + [-1]
