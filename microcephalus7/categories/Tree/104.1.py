# BFS
# 선입선출
# deque
# deque에 추가한 다음 모든 deque 돌며 자손 여부 파악
# 자손 있을 시 count+1 없을 시 return
from collections import deque


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        queue = deque()
        queue.append(root)
        if(root is None):
            return 0
        count = 1
        n2 = 1
        while queue:
            for _ in range(n2):
                i = queue.popleft()
                if(i.left):
                    queue.append(i.left)
                if(i.right):
                    queue.append(i.right)
            n2 = len(queue)
            if(n2 != 0):
                count += 1
        return count
