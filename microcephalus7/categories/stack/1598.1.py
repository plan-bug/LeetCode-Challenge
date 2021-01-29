from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            if i == './':
                continue
            elif i == '../':
                if len(stack) == 0:
                    continue
                stack.pop()
            else:
                stack.append(i)
        return len(stack)
