# DFS
# list 둠
# root값이 Node 이 될 때 list 합 sum

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
