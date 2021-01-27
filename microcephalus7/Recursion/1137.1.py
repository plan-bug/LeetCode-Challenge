class Solution:
    solutions = {
        0:0,1:1,2:1
    }
    def tribonacci(self, n: int) -> int:
        if n in self.solutions:
            return self.solutions[n]
        solution = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        self.solutions[n] = solution
        return solution
        