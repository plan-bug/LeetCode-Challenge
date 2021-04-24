# 극대값
# 전체, 부분 배열에서 가장 중요한 건 극대값
# 증가하는 배열은 극대값이 중요함
# 극대값에 따라 연산만 해주면 됨

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        prev = 0
        for i in nums:
            if i <=prev:
                prev+=1
                count +=prev-i
            else :
                prev = i
        return count