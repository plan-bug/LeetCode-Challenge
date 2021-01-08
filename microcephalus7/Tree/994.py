# 필요 조건
# 각 node 들의 depth
# 각 node 들의 부모 노드 값

# 아이디어
# x, y 중에 일치하는 node 찾으면 해당 node 의 depth, parent node value 값 생성
# 둘 다 나올 때 까지 비교 후 나왔을 경우 parent와. depth 값 비교해서 True/False 반환
# 둘 중 하나 안 나왔을 경우 False 반환
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        results = []
        stack = [[root, None, 0]]
        while stack:

            node, parent, depth = stack.pop()
            if node:
                if node.val == x:
                    results.append((parent, depth))
                if node.val == y:
                    results.append((parent, depth))

                stack.append((node.left, node.val, depth+1))
                stack.append((node.right, node.val, depth+1))
        x, y = results
        return x[0] != y[0] and x[1] == y[1]
