# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def getDecimalValue(self, head: ListNode) -> int:
        arr = self.get_list_node(head)
        # list(map()) 방식을 사용해서 이진수를 만들어도된다.
        digit = len(arr) - 1
        b = 0
        for n in arr:
            b += (10**digit) * n
            digit -= 1
        return int(str(b), 2)

    
    def get_list_node(self, head):
        arr = []
        while True:
            arr.append(head.val)
            if head.next:
                head = head.next
            else:
                return arr
