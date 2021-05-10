class Solution:
    
    def middleNode(self, head: ListNode) -> ListNode:
        arr = []
        count = 0
        def helper(node):
            nonlocal count
            if node:
                arr.append(node)
                count +=1
                helper(node.next)
            return arr[count//2]
        return helper(head)
