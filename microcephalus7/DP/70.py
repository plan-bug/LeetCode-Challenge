class Solution:
    def climbStairs(self, n: int) -> int:
        if not n:
            return 0
        bf = []
        for i in range(n):
            if i == 1:
                bf.append(i)
                break
            combination = []

        return sum(bf)
        1 = [1] = 1
        2 = [[1, 1], [2]] = 2 = 1*1 + 1*1
        3 = [[1, 1, 1], [2, 1], [1, 2]] = 3 = 1 * 1 + 1*2
        4 = [[1, 1, 1, 1], [2, 1, 1], [1, 2, 1], [1, 1, 2], [2, 2]] = 5 = 1*1 + 1*3 + 1*1
        5 = [[1, 1, 1, 1, 1], [2, 1, 1, 1], [1, 2, 1, 1], [1, 1, 2, 1], [1, 1, 1, 2], [2, 2, 1], [1, 2, 2], [2, 1, 2]] = 8 = 1*1 + 1*4 + 1*3
        6 = [[1, 1, 1, 1, 1, 1], [2, 1, 1, 1, 1], [1, 2, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 2, 1], [1, 1, 1, 1, 2], [1, 1, 2, 2]]


solution = Solution()
print(solution.climbStairs(0))