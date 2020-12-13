class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        depth = 0
        while stack:
            cur, cur_depth = stack.pop()
            if cur:
                depth = max(depth, cur_depth)
                if cur.left:
                    stack.append((cur.left, cur_depth+1))
                if cur.right:
                    stack.append((cur.right, cur_depth+1))
        return depth
