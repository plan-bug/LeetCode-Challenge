# DFS
# result 값 담을 list 생성

# 방법 1
# 재귀

# 방법 2
# stack 후 reversed

class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []

        def plusPath(node):
            path = ""
            if node:
                path += str(node.val)

                if node.left:
                    plusPath(node.left)
                if node.right:
                    plusPath(node.right)
                if not node.left and not node.right:
                    paths.append(path)

        plusPath(root)
        return paths
