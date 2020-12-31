# DFS
# result 값 담을 list 생성

# 방법 1
# 재귀

# 방법 2
# stack 후 reversed

class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        path = ""
        if not root:
            return None
        path += str(root.val)

        def plusPath(node, path):

            if node:
                path += "->"
                path += str(node.val)

                if node.left:
                    plusPath(node.left, path)
                if node.right:
                    plusPath(node.right, path)
                if not node.left and not node.right:
                    paths.append(path)
        if root.left:
            plusPath(root.left, path)
        if root.right:
            plusPath(root.right, path)
        if not root.left and not root.right:
            paths.append(path)

        return paths
