from collections import deque


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def helper(node, mirror):
            traversalDeque = deque([node])
            mirrorDeque = deque([mirror])

            while traversalDeque:
                cur, clone = traversalDeque.pop(), mirrorDeque.pop()
                if cur:
                    if cur is target:
                        yield clone
                    traversalDeque.append(cur.left)
                    traversalDeque.append(cur.right)

                    mirrorDeque.append(clone.left)
                    mirrorDeque.append(clone.right)
        return next(helper(original, cloned))
