# DFS
# 재귀
# node 의 , left/right 둘 다 있을 때 catch가 중요
# list 두고 값 얻어내기
# left list, right list

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return None
        results = []

        def plusNode(node, array):
            if node:
                array.append(node.val)
                plusNode(node.left, array)
                plusNode(node.right, array)
            return array
