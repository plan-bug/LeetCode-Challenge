# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    max_depth = 0
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.max_find(root, 0)
        self.find(root, 0)
        return self.result
    
    def max_find(self, tree, depth):
        if tree:
            self.max_depth = max(self.max_depth, depth)
            
            if tree.right:
                self.max_find(tree.right, depth+1)
            
            if tree.left:
                self.max_find(tree.left, depth+1)
    
    def find(self, tree, depth):
        if tree:
            if tree.right:
                self.find(tree.right, depth+1)
            
            if tree.left:
                self.find(tree.left, depth+1)
                
            if (not tree.right) and (not tree.left):
                if self.max_depth == depth:
                    self.result += tree.val
