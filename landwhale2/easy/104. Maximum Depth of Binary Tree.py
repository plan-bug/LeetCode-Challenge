# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    _max = 1
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.b(root, 1)
        return self._max
    
    def b(self, node, cnt):
        if node is None:
            return
        
        if node.left:
            self.b(node.left, cnt+1)
        
        if node.right:
            self.b(node.right, cnt+1)
        
        self._max = max(self._max, cnt)
        
        return
        
        
