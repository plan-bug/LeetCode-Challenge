# 큐 활용
# 큐에 root 추가
# root 값 처리
# root의 left, right 큐에 추가
# 앞 부분 정리
# while 문 이용

from collections import deque


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return root.val + self.rangeSumBST(root.left, low, high)+self.rangeSumBST(root.right, low, high)
