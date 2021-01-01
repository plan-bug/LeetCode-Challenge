# DFS
# result 값 담을 list 생성

# 방법 1
# 재귀

# 방법 2
# stack 후 reversed

class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []

        def plusPath(node, path):

            if node:

                path.append(str(node.val))

                if node.left:
                    plusPath(node.left, path[:])
                if node.right:
                    plusPath(node.right, path[:])
                if not node.left and not node.right:
                    paths.append("->".join(path))
        plusPath(root, [])
        return paths
