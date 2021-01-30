# 잘랐다가 합치기
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))