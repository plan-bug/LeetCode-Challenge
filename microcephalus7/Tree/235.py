# 필요 조건
# p, q 루트의 모든 조상

# 아이디어
# 재귀
# 루트 얻기

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val)) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
