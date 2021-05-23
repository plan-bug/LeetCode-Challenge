class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        q = deque()
        
        q.append((root,-inf))
        
        while q:
            node,maxVal = q.popleft()

            if node.val >= maxVal:
                ans +=1
            
            if node.left:
                q.append((node.left,max(maxVal, node.val)))
            
            if node.right:
                q.append((node.right, max(maxVal, node.val)))
        
        return ans