# 조건
# 루트에서 좌 노드, 우 노드를 비교해야 함
#

# 솔루션 1
# BFS
# 루트 노드의 left, right 의 val 들 추출
# left/right 뒤집은게 같은지 안 같은지 return
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
