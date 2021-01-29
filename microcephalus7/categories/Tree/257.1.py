class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []

        def dfs(node, path):
            if node and node.left and node.right:
                res.append("->".join(path))
            if node.left:
                dfs(node.left, path+[str(node.left.val)])
            if node.right:
                dfs(node.right, path+[str(node.right.val)])
        dfs(root, [str(root.val)])
        return res
