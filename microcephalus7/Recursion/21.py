from typing import List


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        arr = []
        def collector(node):
            nonlocal arr
            if node:
                arr.append(node.val )
                collector(node.next)
        collector(l1)
        collector(l2)
        arr = sorted(arr, reverse=True)
        newList = ListNode()
        runner = newList
        while arr:
            value = arr.pop()
            runner.next = ListNode(value)
            runner = runner.next
        return newList.next


        
        