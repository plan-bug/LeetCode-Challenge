from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            url = i[:-1]
            if url == '.':
                continue
            elif url == '..':
                if len(stack) == 0:
                    continue
                stack.pop()
            else:
                stack.append(i)
        return len(stack)
