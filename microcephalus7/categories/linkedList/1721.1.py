class ListNode:
    def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) :
        first = last = head
        for i in range(k-1):
            first = first.next
        
        nullChecker = first
        while nullChecker.next:
            last = last.next
            nullChecker = nullChecker.next
        first.val, last.val = last.val, first.val
        return head
        