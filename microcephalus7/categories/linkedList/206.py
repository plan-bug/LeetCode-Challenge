class ListNode:
    def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # head = [1,3,5,7,9]
        prev, curr = None, head
        # prev = None, curr = [1,3,5,7,9]
        while curr is not None:
            next = curr.next
            # next = [3,5,7,9]
            curr.next = prev
            # curr.next = None
            # curr = [1]
            prev = curr
            # prev = [1]
            curr = next
            # curr = [3, 5, 7, 9]
        return prev

