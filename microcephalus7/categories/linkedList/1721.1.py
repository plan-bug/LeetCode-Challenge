# 시작/끝 인덱스의 특성을 간파함
# 왜 알 수 있었을까?
# 추론력!
# 여러 linkedListLength, index 값을 가지고 특징을 찾음  

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
        