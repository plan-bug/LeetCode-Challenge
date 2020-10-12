# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    root = None
    
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.root = root
        result = 0
        for i in range(L, R+1):
            if self.find(i):
                result += i
        return result
    
    def find(self, val):
        if (self.findNode(self.root, val) is False):
            return False
        else:
            return True

    def findNode(self, currentNode, val):
        if (currentNode is None):
            return False
        elif (val == currentNode.val):
            return currentNode
        elif (val < currentNode.val):
            return self.findNode(currentNode.left, val)
        else:
            return self.findNode(currentNode.right, val)
