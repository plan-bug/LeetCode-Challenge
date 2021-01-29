# 필요조건
# 각 left, right 의 서브 노드 유/무

# BFS
# node 들 돌며 height list 에 모음
# list 에서 max, min 에서 차이 i 이상 에 따라 True/False

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1+max(left, right)
        return check(root) != -1
