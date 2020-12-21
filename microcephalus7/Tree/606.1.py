class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t == None:
            return ""

        if t.left == None and t.right == None:
            return str(t.val)

        leftString = self.tree2str(t.left)
        rightString = self.tree2str(t.right)

        if rightString == "":
            return str(t.val) + "("+leftString+")"

        else:
            return str(t.val)+"("+leftString+")"+"("+rightString+")"
