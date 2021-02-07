# 2진수 이용
# 2진수로 변환 후 
class Solution:
    def numberOfSteps(self, num:int)-> int:
        bitString = bin(num)[2:]
        return len(bitString) -1 - bitString.count('1')