# dfs
# backtracking

# 전제 조건
# 부모 노드를  return 할 수 있어야 함

# Deepest Leaves 의 부모 전제 조건
#

# Leave 의 조건
# 자식이 없어야 함

# Deepest Leaves 의 조건
# 깊이를 알아야 하며 제일 깊다는 것을 알아야 함
# 밑에 자식이 없어야 함
#


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        self.lca, self.deepest = None, 0

        def helper(node, depth):
            self.deepest = max(self.deepest, depth)
            if not node:
                return depth
            left = helper(node.left, depth + 1)
            right = helper(node.right, depth + 1)
            if left == right == self.deepest:
                self.lca = node
            return max(left, right)

        helper(root, 0)
        return self.lca
