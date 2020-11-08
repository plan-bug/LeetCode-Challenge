class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def remove(num):
            nums2.remove(num)
            return num
        return [remove(i) for i in nums1 if i in nums2]
