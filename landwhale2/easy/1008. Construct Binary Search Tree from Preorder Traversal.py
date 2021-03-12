# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
        if len(preorder)==0:
            return
    
        idx=sorted(preorder).index(preorder[0])
        node=TreeNode(preorder[0])
        node.left=self.bstFromPreorder(preorder[1:idx+1])
        node.right=self.bstFromPreorder(preorder[idx+1:])
        return node
