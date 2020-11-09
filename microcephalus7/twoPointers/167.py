# two pointer 문제
# start, end 두 변수 둠
# while 문
# if 문으로 continue 통제
# while 문으로 돌며 맞는 start,end 찾을 시 return


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i, e in enumerate(numbers):
            if e in dict:
                return (dict[e], i+1)
            dict[(target - e)] = i+1
        return list(dict)


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([2, 3, 4], 6))
print(solution.twoSum([5, 25, 75], 10))
