# dp
# for 문
# nums 의 첫 요소를 변수로 둚
# 
# for 문 돌며 각 요소를 변수와 비교
# for 문 돌며 변수와 요소를 비교해서 값이 같거나 적으면 1씩 올리고 count+=1 for문 다시 시작
# for 끝나면 count return

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