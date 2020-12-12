# 방법 1
# root.val 을 변수1로 둠
# 루프 돌며 node.val 이 변수1과 다를 경우 false
# 루프 끝나면 true

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        num = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val != num:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True
