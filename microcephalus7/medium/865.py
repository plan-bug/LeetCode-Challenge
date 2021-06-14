class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        self.lca = None
        self.deepest = 0

        def backtraking(node, depth):
            self.deepest = max(self.deepest, depth)
            if not node:
                return depth
            left = backtraking(node.left, depth + 1)
            right = backtraking(node.right, depth + 1)
            if left == right == self.deepest:
                self.lca = node
            return max(left, right)

        backtraking(root, 0)
        return self.lca
