# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    new_root = None
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = self.find(root, [])
        self.new_root = self.insert(self.new_root, sorted(arr), 0)
        return self.new_root
    
    def find(self,root, arr):
        if root is None:
            return
        arr.append(root.val)
        
        if root.left is not None:
            self.find(root.left, arr)
        
        if root.right is not None:
            self.find(root.right, arr)
        
        return arr
    
    def insert(self, root, arr, head):
        if head == len(arr):
            return
        if root is None:
            root = TreeNode(val=arr[head])

        
        if arr[head] >= root.val:
            
            root.right = self.insert(root.right, arr, head+1)
        
        return root
