class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = []
        while head:
            arr.append(head)
            head = head.next
        return arr[len(arr)//2]