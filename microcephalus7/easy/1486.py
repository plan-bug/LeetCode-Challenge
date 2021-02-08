class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = []
        for i in range(n):
            arr.append(start + i*2)
        res = arr[0]
        for i in arr[1:]:
            res ^=i
        return res