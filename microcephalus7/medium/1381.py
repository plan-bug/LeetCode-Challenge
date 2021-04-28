# stack 구조 생성
# 매 함수마다 길이 값 판별 후 수행

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        
    def push(self, x: int) -> None:
        stack = self.stack
        if len(stack) >= self.maxSize:
            return 
        stack.append(x)
        
    def pop(self) -> int:
        stack = self.stack
        if stack:
            return stack.pop()
        return -1
        
    def increment(self, k: int, val: int) -> None:
        stack = self.stack
        stackLen = len(stack)
        for i in range(min(k,stackLen)):
            stack[i]+=val
        
        