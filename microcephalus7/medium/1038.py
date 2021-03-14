class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def recur (node, res):
            if not node:
                return res
            node.val += recur(node.right,res)
            return recur(node.left,node.val)
        recur(root,0)
        return root