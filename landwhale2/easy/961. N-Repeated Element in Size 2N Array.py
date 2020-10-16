from collections import Counter

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        n_count = {}
        for a in A:
            try:
                n_count[a] += 1
            except:
                n_count[a] = 1
        inverse = [(value, key) for key, value in n_count.items()]

        return max(inverse)[1]
