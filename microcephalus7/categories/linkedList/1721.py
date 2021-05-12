# 모든 노드 값 list 에 수집
# k 에 따른 교체
# 교체 시킨 list 기반 Node 생성
# Node return

class ListNode:
    def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) :
        arr = []
        def collector(node):
            if node:
                arr.append(node.val)
                collector(node.next)
        collector(head)
        arrLength = len(arr)
        start = arr[k-1]
        end = arr[arrLength-k]
        arr[k-1] = end
        arr[arrLength-k] = start
        newNode = ListNode()
        nextNode = newNode
        for i in range(arrLength):
            nextNode.val = arr[i]
            if i ==arrLength-1:
                break
            nextNode.next = ListNode()
            nextNode = nextNode.next
        return newNode

        
