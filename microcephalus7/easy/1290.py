class Solution:
    
    def getDecimalValue(self, head: ListNode) -> int:
        result = ""
        while head:
            result += str(head.val)
            head = head.next
        return int(result,2)