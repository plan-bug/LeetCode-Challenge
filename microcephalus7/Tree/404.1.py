# stack 시 튜플로 묶기
# left 의 경우 True, right 의 경우 False 로 한 후 True/False 에 따라 연산

class Solution:

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result = 0
        stack = [(root, False)]
        while stack:
            curr, isLeft = stack.pop()
            if not curr:
                continue
            if not curr.left and not curr.right:
                if isLeft:
                    result += curr.val
            else:
                stack.append((curr.left, True))
                stack.append((curr.right, False))
        return result
