# collection 생성
# value 값 모은 list 생성
# list 를 다시 Counter
# 컴프레션으로 1보다 큰 수만 모은 후 빈 배열일 시 True 아니면 False

from typing import List

from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return [i for i in Counter(Counter(arr).values()).values() if i > 1] == [] and True or False
