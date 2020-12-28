# stack
# 튜플로 묶어서 반복 진행

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while len(stack):
            first, second = stack.pop()
            if not first and not second:
                pass
            elif not first or second:
                return False

            else:
                if first.val != second.val:
                    return False
                stack.append((first.left, second.left))
                stack.append((first.right, second.right))
        return True
