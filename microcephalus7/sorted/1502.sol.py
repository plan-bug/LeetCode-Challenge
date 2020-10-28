# 처음부터 차이 return
# 다음 요소와 차이의 합이 그 다음 요소 값이 아닐 경우 False return

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]

        for i in range(1, len(arr) - 1):
            if arr[i] + diff != arr[i + 1]:
                return False

        return True
