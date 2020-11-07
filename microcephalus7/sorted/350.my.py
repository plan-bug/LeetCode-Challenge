from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        array = []
        for i in nums1:
            if i in nums2:
                array.append(i)
                nums2.remove(i)
        return array
