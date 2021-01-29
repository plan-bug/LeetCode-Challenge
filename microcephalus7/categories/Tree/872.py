# DFS
# 모든 node 순회하며 left, right 없을 때 list에 더함
# 왼쪽부터 순회해야 하므로 reverse
# 각 list 비교한 후 True/False

# 방법 1
# 재귀

# 방법 2
# 순회

class Solution:
    def __init__(self) -> None:
        self.result1 = []
        self.result2 = []

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def compare(arr, result):
            if arr.left:
                compare(arr.left, result)
            if arr.right:
                compare(arr.right, result)
            if not arr.left and not arr.right:
                result.append(arr.val)
            return result
        return compare(root1, self.result1) == compare(root2, self.result2)
