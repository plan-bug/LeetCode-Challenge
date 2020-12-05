# 방법 1
# 기존의 Node 중 하나를 선택하고 다른 노드를 더함

# 방법 2
# 새로운 노드를 생성하고 매 노드 돌며 두 노드를 더함
# 매 층계마다 같은 순서로 가야함

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        elif not t2:
            return t1
        else:
            res = TreeNode(t1.val+t2.val)
            res.left = self.mergeTrees(t1.left, t2.left)
            res.right = self.mergeTrees(t1.right, t2.right)
