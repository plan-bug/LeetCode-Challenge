class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.height(root)
        return self.isBalanced

    def height(self, node):
        if not node:
            return 0
        left = self.height(node.left)
        right = self.height(node.right)
        if abs(left-right) > 1:
            self.isBalanced = False
        return max(left, right)+1
