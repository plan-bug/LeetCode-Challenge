
from collections import deque

# DFS
# 재귀로 이터러블


class Solution:
    def __init__(self) -> None:
        self.valList = []

    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        self.valList.append(root.val)
        if root.children:
            for i in root.children:
                self.preorder(i)
        return self.valList
