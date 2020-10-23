from typing import List


class Solution:
    def restoreString(self, string: str, indices: List[int]) -> str:
        strings = [(sValue, index)
                   for sValue, index in zip(list(string), indices)]
        return ''.join([sval[0] for sval in sorted(strings, key=lambda x: x[1])])
