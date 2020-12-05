class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack = [root]
        total = 0
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    total += node.val
                stack.append(node.left)
                stack.append(node.right)
        return total
