# stack 으로 풀기
# 모든 노드 돌며 t.val 과 비교
# 같을 시 모든 노드 도는 함수에 넣음
# stack 으로 안될떄가 있다
# 

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def traverseTree(s):
            if s:
                return f"#{s.val} {traverseTree(s.left)} {traverseTree(s.right)}"
        return traverseTree(t) in traverseTree(s)
        