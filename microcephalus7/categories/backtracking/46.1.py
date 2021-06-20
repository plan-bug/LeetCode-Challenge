class Solution:
    def permute(self, nums):
        return reduce(
            lambda P, n: [p[:i] + [n] + p[i:] for p in P for i in range(len(p) + 1)], nums, [[]]
        )
