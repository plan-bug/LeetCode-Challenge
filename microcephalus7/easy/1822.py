# 배열 다루기
# 0 이 nums 안에 있다면 return 0
# 아닐 시 reduce 로 원소 곱한 뒤 결과에 따라 return 1 or -1

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        else :
            return reduce(lambda x, y: x * y, nums) > 0 and 1 or -1 