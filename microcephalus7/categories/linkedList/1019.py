# arr(list) 에 node collection
# for i in range(arr)
# i 뒤 arr 커팅 후 max(arr) 와 i 비교 
# res(list)
# i 가 max(arr) 보다 크거나 같을 시 res.append(0)
# 작을 시 append(max(arr))

class ListNode:
    def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res, stack = [],[]
        while head:
            while stack and stack[-1][1]<head.val:
                res[stack.pop()[0]]= head.val
            stack.append([len(res),head.val])
            res.append(0)
            head=head.next
        return res
        
        

