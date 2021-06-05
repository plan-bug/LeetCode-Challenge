# dfs/bfs 로 arr(list) node val 모음
#  arr 정렬 후 arr[k] return


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        stack = [root]
        while stack:
            newNode = stack.pop()
            if newNode:
                res.append(newNode.val)
                stack.append(newNode.left)
                stack.append(newNode.right)
        return sorted(res)[k - 1]
