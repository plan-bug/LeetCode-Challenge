# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        val_p = list()
        val_q = list()
        
        def find(tree, val) -> list:

            if tree:
                val.append(tree.val)
                
                if tree.left:
                    find(tree.left,val)
                else:
                    val.append(None)
                
                if tree.right:
                    find(tree.right,val)
                else:
                    val.append(None)
            
            return val

        return find(p,val_p) == find(q,val_q)  
