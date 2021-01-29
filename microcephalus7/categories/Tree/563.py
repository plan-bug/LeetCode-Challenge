# left, right 각 노드 순회
# 노드 없을 땐 0
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
