# DFS
# 재귀
# node 추가하는 과정에 괄호 넣는 작업
class Solution:
    def __init__(self) -> None:
        self.result = ""

    def tree2str(self, t: TreeNode) -> str:
        self.result += "("
        if t:
            self.result += str(t.val)
            if t.right:
                self.tree2str(t.left)
                self.tree2str(t.right)
            else:
                if t.left:
                    self.tree2str(t.left)
        self.result += ")"
        return self.result
