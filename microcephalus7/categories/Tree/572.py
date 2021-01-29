# dfs, bfs 상관없음
# 모든 노드 돌며 비교할 줄 아느냐를 묻는 문제

# 의문접 1
# 왜 단순 비교식은 안 되는건가?
#  
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        if t is None:
            return True

        if s is None:
            return False
        if s.val == t.val:
            if self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right):
                return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right,t)
        
    def isSameTree(self,s,t):
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False
        if s.val == t.val:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
                