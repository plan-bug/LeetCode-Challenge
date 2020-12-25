# BST 돌며 모든 수 list
# list 내부에서 값 차이로 만든 list 생성(절대값 메서드 사용)
# 새 list에서 최소값 return

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return None
        values = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                values.append(node)
                stack.append(node.left)
                stack.append(node.right)
        newValues = []
        i = 0
        j = 1
        while j == len(values):
            if i == j:
                i == 0
                j += 1
            newValues.append()
