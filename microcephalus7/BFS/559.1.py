# 각 Node 의 children 들을 나열하고 그걸 list 에 새로 담는 형식
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        stack = [root]
        res = 0
        while stack:
            tem = []
            res += 1
            for i in stack:
                for j in i.children:
                    tem.append(j)
            stack = tem[:]
        return res
