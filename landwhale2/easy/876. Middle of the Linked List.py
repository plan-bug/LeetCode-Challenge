# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    cut = 0
    def middleNode(self, head: ListNode) -> ListNode:
        new_head = ListNode()
        self.cut = self.length(head, 0) // 2
        return self.get_node(head, new_head, 0)
    
    def length(self,node, cnt):
        if node is None:
            return cnt
        else:
            return self.length(node.next, cnt+1)
    
    def get_node(self, head, new_head, cnt):
        if head is None:
            return
        if head.val and self.cut <= cnt:
            new_head.val = head.val
            new_head.next = head.next
        
        if head.next and new_head.next:
            self.get_node(head.next, new_head.next, cnt + 1)
        elif head.next:
            self.get_node(head.next, new_head, cnt + 1)
        
        return new_head
