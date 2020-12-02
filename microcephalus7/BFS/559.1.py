
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
