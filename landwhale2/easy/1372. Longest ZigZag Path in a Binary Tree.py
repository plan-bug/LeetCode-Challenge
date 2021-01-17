class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def find(node, l=0, r=0):
            if node:
                res[0] = max(res[0], l, r)
                find(node.left, 0, l+1)
                find(node.right, r+1, 0)
            
        res = [0]
        find(root)
        return res[0]
