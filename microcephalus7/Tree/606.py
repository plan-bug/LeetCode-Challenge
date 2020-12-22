# DFS
# 재귀
# node 추가하는 과정에 괄호 넣는 작업
class Solution:
    def __init__(self) -> None:
        self.result = ""

    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return self.result

        self.result += str(t.val)

        def string(node):
            self.result += "("
            if node:
                self.result += str(node.val)
                if node.right:
                    string(node.left)
                    string(node.right)
                else:
                    if node.left:
                        string(node.left)
            self.result += ")"
        if t.right:
            string(t.left)
            string(t.right)
        else:
            if t.left:
                string(t.left)
        return self.result
