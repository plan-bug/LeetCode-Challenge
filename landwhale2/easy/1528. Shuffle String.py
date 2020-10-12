class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [0] * len(s)
        for st, i in zip(s, indices):
            arr[i] = st
        return ''.join(arr)
            
