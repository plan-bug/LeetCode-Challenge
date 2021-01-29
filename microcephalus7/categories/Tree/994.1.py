class Solution:

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        results = []

        def cousins(node, parent, depth, x, y):
            if node:
                if node.val == x or node.val == y:
                    results.append((parent, depth))
                cousins(node.left, node.val, depth+1, x, y)
                cousins(node.right, node.val, depth+1, x, y)

        cousins(root, None, 0, x, y)
        x, y = results
        return x[0] != y[0] and x[1] == y[1]
