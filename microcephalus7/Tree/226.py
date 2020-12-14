# 방법 1
# 새로운 Tree 생성

# 방법 2
# 기존의 Tree 수정

# 재귀


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        def invert(node):
            if node.left or node.right:
                nodeLeft = node.left
                nodeRight = node.right
                node.left = nodeRight
                node.right = nodeLeft
                if node.left:
                    invert(node.left)
                if node.right:
                    invert(node.right)
        invert(root)
        return root
