
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(L, R):
            if not L and not R:
                return True
            elif L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            else:
                return False
        return isSym(root, root)
