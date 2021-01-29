# 재귀 함수와 값 얻는 함수로 나누기
class Solution:
    def __init__(self) -> None:
        self.result = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        if not root:
            return 0

        def recur(node, boolean):
            if node:
                if not node.left and not node.right:
                    if boolean:
                        self.result += node.val
                else:
                    recur(node.left, True)
                    recur(node.right, False)

        recur(root, False)

        return self.result
