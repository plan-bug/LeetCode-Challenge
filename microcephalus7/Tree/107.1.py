# DFS
# queue 구조
# 각 list에 담은 후 reverse 된 list return

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        result = []
        queue = [root]
        while queue:
            newQueue = []
            newResult = []
            for i in queue:
                if i:
                    newResult.append(i.val)
                    newQueue.append(i.left)
                    newQueue.append(i.right)
            queue = newQueue
            if newResult:
                result.append(newResult)
        return reversed(result)
