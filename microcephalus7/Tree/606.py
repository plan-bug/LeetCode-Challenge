# DFS
# 재귀
# node 추가하는 과정에 괄호 넣는 작업
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return None
        result = ""
        result += str(t.val)

        def string(node, result):
            result += "("
            if node:
                result += str(node.val)
                string(node.left, result)
                string(node.right, result)
            result += ")"

        string(t.left, result)
        string(t.right, result)
        return result
