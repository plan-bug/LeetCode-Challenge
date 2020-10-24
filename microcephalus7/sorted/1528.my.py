# string 요소와 index 묶음
# index 값 기준으로 정렬 후 string 값 return

from typing import List


class Solution:
    def restoreString(self, string: str, indices: List[int]) -> str:
        strings = [(sValue, index)
                   for sValue, index in zip(list(string), indices)]
        return ''.join([sval[0] for sval in sorted(strings, key=lambda x: x[1])])
