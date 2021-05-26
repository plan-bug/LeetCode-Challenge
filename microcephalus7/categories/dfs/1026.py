class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        maxDif = 0
        
        def dfs(node,a,b):
            nonlocal maxDif
            if node:
                a, b =min(a,node.val), max(b, node.val)
                maxDif = max(maxDif, b-a)

                dfs(node.left, a,b)
                dfs(node.right, a, b)

        dfs(root, float("inf"), float("-inf"))
            
            
        return maxDif