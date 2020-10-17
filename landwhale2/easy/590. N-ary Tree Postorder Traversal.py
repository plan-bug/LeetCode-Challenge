"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        arr = self.find(root, result)
        return arr
    
    def find(self,root, result):
        if root is None:
            return
        
        for child in root.children:
            self.find(child, result)
            
        
        result.append(root.val)
        return result
        
        
        
        
