# 피보나치

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 :
            return 0
        if n == 1:
            return 1
        first, second = 0,1
        for i in range(n-1):
            newNumber = first + second
            first = second
            second = newNumber
        return second
