class Solution:
    def __init__(self) -> None:
        self.s = 0
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def rec (node, parent, grand):
            if node:
                if grand%2 == 0:
                    self.s+=node.val
                rec(node.left, node.val, parent)
                rec(node.right, node.val, parent)
        rec(root,1,1)
        return self.s