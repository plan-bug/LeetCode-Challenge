# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        return True if len(list(set(self.find(root, [])))) == 1 else False
    
    def find(self,root, arr):
        if root is None:
            return
        arr.append(root.val)
        
        if root.left is not None:
            self.find(root.left, arr)
        
        if root.right is not None:
            self.find(root.right, arr)
        
        return arr
