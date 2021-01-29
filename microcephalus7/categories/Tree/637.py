# BFS
# queue 이용
# 각 층계 돌 떄 마다 list에 값 넣고 길이 만큼 나눈 뒤 result에 삽입

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return None
        queue = [root]
        result = []
        while queue:
            newResult = []
            newQueue = []
            for i in queue:
                newResult.append(i.val)
                if i.left:
                    newQueue.append(i.left)
                if i.right:
                    newQueue.append(i.right)
            result.append(sum(newResult)/len(newResult))
            queue = newQueue[:]
        return result
