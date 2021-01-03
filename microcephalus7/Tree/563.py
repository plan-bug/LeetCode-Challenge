# DFS
# 재귀
# node 의 , left/right 둘 다 있을 때 catch가 중요
# list 두고 값 얻어내기

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.tilt = 0

        def computeSum(node):
            if not node:
                return 0
            leftSum = computeSum(node.left)
            rightSum = computeSum(node.right)
            self.tilt += abs(leftSum-rightSum)
            treeSum = leftSum+node.val+rightSum
            return treeSum
        computeSum(root)
        return self.tilt
