# dp
# 모든 노드 돌며 val 담은 list 생성
# list 정렬 후 for문으로 (i + 1) - (i -1) 한 값 중 최솟값 찾기
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:
            return None
        stack = [root]
        values = []
        while stack:
            node = stack.pop()
            if node:
                values.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        values = sorted(values)
        minimum = values[1] - values[0]
        for i in range(2, len(values)):
            minimum = min([minimum, values[i]-values[i-1]])
        return minimum
