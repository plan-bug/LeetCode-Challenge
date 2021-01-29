# 중간에서 왼쪽과 오른쪽이 길이가 같다는 것 이용
# list 자르는 작업 반복
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        def helper(treelist):
            if len(treelist) == 0:
                return None
            if len(treelist) == 1:
                return TreeNode(treelist[0])
            mid = len(treelist)//2
            treelist[mid] = TreeNode(treelist[mid])
            treelist[mid].left = helper(treelist[:mid])
            treelist[mid].right = helper(treelist[mid+1:])
            return treelist[mid]
        return helper(nums)


solution = Solution()
print(solution.sortedArrayToBST([1, 3, 4, 5]))
