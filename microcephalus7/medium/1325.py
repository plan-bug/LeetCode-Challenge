# dfs, bfs 관계 없이 node 탐색 및 제거
# 자녀 유/무 판별 필요

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def dfs(node):
            if node:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                if not node.left and not node.right and node.val == target:
                    return None
                return node
        root = dfs(root)
        return root