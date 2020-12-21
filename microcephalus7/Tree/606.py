# DFS
# 재귀
# node 추가하는 과정에 괄호 넣는 작업
class Solution:
    def __init__(self) -> None:
        self.result = ""

    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return None

        self.result += str(t.val)

        def string(node):
            if node:
                self.result += "("
                self.result += str(node.val)
                string(node.left)
                string(node.right)
                self.result += ")"

        string(t.left)
        string(t.right)
        return self.result
