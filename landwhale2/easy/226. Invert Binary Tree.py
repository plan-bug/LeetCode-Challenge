class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if(root==None):
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        l=root.left
        root.left=root.right
        root.right=l
        return root
