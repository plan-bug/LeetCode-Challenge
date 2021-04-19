# node 모으는 함수 생성
# 함수 return 값으로 list
# list extend 로 합친 후 sorted

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        def collector(node):
            if node:
                res.append(node.val)
                collector(node.left)
                collector(node.right)
        collector(root1)
        collector(root2)
        return sorted(res)
