# DFS
# left, right 가 없을때 까지 while
# 문자열은 더 하면 추가됨

class Solution:

    def sumRootToLeaf(self, root: TreeNode) -> int:
        total = 0
        stack = [(root, str(root.val))]
        while stack:
            node, binVal = stack.pop()
            if node.left:
                stack.append((node.left, binVal+str(node.left.val)))

            if node.right:
                stack.append((node.right, binVal+str(node.right.val)))

            if not node.left and not node.right:
                total += int(binVal, 2)
        return total
