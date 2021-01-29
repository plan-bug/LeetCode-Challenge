# 풀이
# l1, l2 둘 다 sorted 됨
# l1, l2 비교하며 작은 쪽을 가져옴
# 한 쪽이 남았을 경우를 대비하여 next 에 투입
# 참조하고 있는 다른 node return

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = sortList = ListNode(0)

        while (l1 and l2):
            if (l1.val < l2.val):
                sortList.next =l1
                l1= l1.next
                sortList = sortList.next
            else :
                sortList.next = l2
                l2 = l2.next
                sortList = sortList.next
        sortList.next = l1 or l2
        return head.next