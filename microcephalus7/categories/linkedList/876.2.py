class Solution:
    def __init__(self) -> None:
        self.arr = []
    def middleNode(self, head: ListNode) -> ListNode:
        if head:
            self.arr.append(head)
            self.middleNode(head.next)
        else:
            return self.arr[len(self.arr)//2]