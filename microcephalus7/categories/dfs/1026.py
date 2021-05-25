class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        maxDif = 0
        
        def dfs(node):
            nonlocal maxDif
            if not node:
                return 0

            left = dfs(node.left)
            right =dfs(node.right)

            maxDif =  max(maxDif, abs())

            return node.val
        dfs(root)
        return maxDif