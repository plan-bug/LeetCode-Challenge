class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        sList = list(s)
        strings = [(sValue, index) for sValue, index in zip(sList, indices)]
        return ''.join([sval[0] for sval in sorted(strings, key=lambda x: x[1])])
