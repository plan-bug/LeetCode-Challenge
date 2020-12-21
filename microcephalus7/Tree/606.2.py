class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        stack = [t]
        visited = set()
        result = []
        while stack:
            t = stack[-1]
            if t in visited:
                stack.pop()
                result.append(')')
            else:
                visited.add(t)
                result.append(f'({t.val}')
                if not t.left and t.right:
                    result.append('()')
                if t.right:
                    stack.append(t.right)
                if t.left:
                    stack.append(t.left)
        return ''.join(result)[1:-1]
