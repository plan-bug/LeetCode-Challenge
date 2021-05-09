# 중간 노드를 알 수 있는 전제 조건
# 전체 Linked List 의 길이
# 해당 Linked List 의 순서

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        original = head
        copy= head
        while copy and copy.next:
            original = original.next
            copy = copy.next.next
        return original