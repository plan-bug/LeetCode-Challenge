# stack
# s 이터러블
# append 로 각 요소 받음
# stack의 마지막 요소 두개 비교해서 유지/삭제

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) > 1:
                if stack[-2].lower() == stack[-1].lower():
                    if stack[-2] != stack[-1]:
                        stack.pop()
                        stack.pop()
        return ''.join(stack)


solution = Solution()
print(solution.makeGood("leEeetcode"))
