# DFS
# queue 형성
# queue val list에 집어 넣음
# children 존재 할 시
# children stack 에 집어넣고 val list 에 집어넣음
from collections import deque


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
