# 2ㅍ인터

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) :
        i = j = res = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                res = max(res, j-i)
                j +=1
        return res