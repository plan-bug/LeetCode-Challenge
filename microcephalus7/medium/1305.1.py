class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        def collector(node):
            stack = [node]
            while stack:
                poped = stack.pop()
                if poped:
                    res.append(poped.val)
                    stack.append(poped.left)
                    stack.append(poped.right)
        collector(root1)
        collector(root2)
        return sorted(res)
        