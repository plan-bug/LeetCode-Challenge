# BackTracking?
# 1이 나오지 않은 node 는 None return?


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and not root.val:
            return None
        return root
