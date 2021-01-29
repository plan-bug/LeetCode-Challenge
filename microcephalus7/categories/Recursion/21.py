# ㅣ1, ㅣ2 list 값들 모음
# 해당 값들 이용해 새로운 ListNde 생성  




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


        
        