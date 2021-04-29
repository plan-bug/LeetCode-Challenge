# TreeNode 에서 모든 수를 가져옴
# 가져온 수로 어떻게 balanced 된 BST 를 만들 지 관건
# sol 1
# 가져온 수의 list 에서 중간 node 가 head 가 됨
# 중간 node 앞 은 head 의 왼팔이 됨
# 중간 node 뒤는 head 의 오른팔이 됨

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        arrayList = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arrayList.append(node.val)
            dfs(node.right)
        dfs(root)
        def create(arrayList):
            if not arrayList:
                return
            middle = len(arrayList) // 2
            newRoot = TreeNode(arrayList[middle])
            newRoot.left = create(arrayList[:middle])
            newRoot.right = create(arrayList[middle+1:])
            return newRoot
        return create(arrayList)
