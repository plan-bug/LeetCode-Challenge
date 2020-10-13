class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        result = 0
        for s,e in zip(startTime, endTime):
            if s <= queryTime <= e:
                result += 1
        return result
