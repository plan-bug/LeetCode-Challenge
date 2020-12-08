# BFS
# 너비 우선으로 탐색하며 해당 node 의 val 이 val 과 같을 경우 해당 node return
# stack 역할하는 list 생성 (root 삽입)
# val 있을때 까지 stack
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val == val:
                    return node
                stack.append(node.left)
                stack.append(node.right)
        return None
