# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum_ = 0
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.find(root,'',0)
        return self.sum_
    
    def find(self, root, b, result):
        if root is None:
            return
        b += str(root.val)
        
        if root.right is None and root.left is None:
            self.sum_ += int(b, 2)
        
        self.find(root.left, b, result)    
        self.find(root.right, b, result)
            
   
        
