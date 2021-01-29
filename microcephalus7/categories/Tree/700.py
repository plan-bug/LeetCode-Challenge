# DFS

# stack 역할하는 list 생성 (root 삽입)
# val 있을때 까지 stack

# BFS 보다 느림
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
                elif node.val > val:
                    stack.append(node.left)
                else:
                    stack.append(node.right)
        return None
