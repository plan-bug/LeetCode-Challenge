# 정렬
# 정렬된 list 1,2 번째 차이 구함
# for문으로 arr[i] 와 arr[i+1] 의 차가 1,2 번째와 차이 같을 시 True/False

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]

        for i in range(1, len(arr) - 1):
            if arr[i] + diff != arr[i + 1]:
                return False

        return True
