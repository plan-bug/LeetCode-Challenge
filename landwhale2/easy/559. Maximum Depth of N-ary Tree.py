"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    cnt_max = 0
    def maxDepth(self, root: 'Node') -> int:
        if root:
            self.find(root, self.cnt_max + 1)
        return self.cnt_max
    
    def find(self, node, cnt):
        if node is None:
            return
        
        if node.children:
            for children in node.children:
                self.find(children, cnt+1)
        self.cnt_max = max(self.cnt_max, cnt)
        
        
