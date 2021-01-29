# node 와 node의 깊이 묶어서 하나로 표현
# 하나의 깊이 마다 +1
# return 값인 depth는 깊이 중 최대값

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
