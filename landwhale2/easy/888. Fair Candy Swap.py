class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        swap_diff, B = (sum(A) - sum(B)) // 2, set(B)
        for a in A:
            if a - swap_diff in B:
                return [a, a - swap_diff]
