class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return filter(lambda num: '0' not in str(num) and all([num%int(digit) == 0 for digit in str(num)]), range(left,right+1))