# stack, pop

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        stack = [root]
        out = []
        while stack:
            temp = stack.pop()
            if temp:
                out.append(temp.val)
                for i in temp.children:
                    stack.append(i)
        return reversed(out)
