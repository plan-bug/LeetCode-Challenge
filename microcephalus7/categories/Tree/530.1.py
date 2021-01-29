class Solution:
    def getMinimumDifference(self, root):
        res = []
        self.traverse(root, res)
        res, m = sorted(res), inf
        for i in range(1, len(res)):
            m = min(m, res[i]-res[i-1])
        return m

    def traverse(self, root, res):
        if not root:
            return
        res.append(root.val)
        if root.left and root.right:
            return self.traverse(root.left, res), self.traverse(root.right, res)
        if root.left:
            return self.traverse(root.left, res)
        if root.right:
            return self.traverse(root.right, res)
