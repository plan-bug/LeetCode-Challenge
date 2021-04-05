class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder:
            root = TreeNode(preorder.pop(0))
            if preorder:
                index = 0
                while index < len(preorder) and preorder[index] <= root.val:
                    index += 1
                root.left = self.bstFromPreorder(preorder[:index])
                root.right = self.bstFromPreorder(preorder[index:])
            return root
