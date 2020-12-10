# stack 구조에 맞게 reversed 로 역정렬
# extend 로 for 문 대신 함

class Solution:

    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        stack = [root]
        out = []
        while stack:
            temp = stack.pop()
            out.append(temp.val)
            stack.extend(reversed(temp.children))
        return out
