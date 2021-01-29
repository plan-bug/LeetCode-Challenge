# 겹치는거 찾기
# set 으로 중복 삭제
# intersection 함수로 겹치는 요소 찾기

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
