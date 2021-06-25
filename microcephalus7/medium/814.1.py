class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.pruneTree(root.left), self.pruneTree(root.right)
        if root and (root.left or root.right or root.val):
            return root
