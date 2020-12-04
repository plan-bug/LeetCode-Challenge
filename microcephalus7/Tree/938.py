class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack = [root]
        ans = 0
        while(stack):
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if high > node.val:
                    stack.append(node.right)
        return ans
