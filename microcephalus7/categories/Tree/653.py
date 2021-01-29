# BFS, DFS 상관 없음
# 모든 node 값 순회해서 list 에 k에서 뺀 수 넣음
# node.val 이 list 안에 있을 경우 True


from typing import Tuple


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return None
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                if node.val in result:
                    return True
                result.append(k-node.val)
                stack.append(node.left)
                stack.append(node.right)
        return False
