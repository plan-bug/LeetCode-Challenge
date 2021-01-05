# 재귀 함수와 값 얻는 함수로 나누기
class Solution:
    def __init__(self) -> None:
        self.result = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        if not root:
            return None

        def recur(node):
            if node.left:
                plus(node.left)
                recur(node.left)
            if node.right:
                recur(root.right)

        def plus(node):
            self.result += node.val
        recur(root)

        return self.result
