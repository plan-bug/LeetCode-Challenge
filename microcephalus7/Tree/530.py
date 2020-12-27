# BST 돌며 모든 수 list
# 정렬 후 DP로 최소 차이값 return

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return None
        values = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                values.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        values = sorted(values)
        minimum = inf
        for i in range(1, len(values)):
            minimum = min(minimum, values[i]-values[i-1])
        return minimum
