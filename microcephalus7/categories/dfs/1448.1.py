class Solution:
    def goodNodes(self, root: TreeNode, ma = -inf) -> int:
        return self.goodNodes(root.left, max(ma, root.val)) + self.goodNodes(root.right, max(ma,root.val)) + (root.val >= ma) if root else 0