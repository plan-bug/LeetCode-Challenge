# 방법 1
# stack 방식으로 모든 node 돌며 list에 삽입
# list 정렬 후 Node 화

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = [root]
        arr = []
        while stack:
            node = stack.pop()
            if node:
                arr.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        arr = sorted(arr, reverse=True)

        arrPop = arr.pop()
        newTree = TreeNode(arrPop)

        def bst(node):
            while arr:
                arrPop = arr.pop()
                node.right = TreeNode(arrPop)
                bst(node.right)
            return node
        return bst(newTree)

        arrPop = arr.pop()
        newTree.right = TreeNode(arrPop)
        arrPop = arr.pop()
        newTree.right.right = TreeNode(arrPop)
