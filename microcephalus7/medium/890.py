# ascii 코드 이용
# pattern ascii 코드로 변환
# 이러터레이러 돌며 pattern element 들 pattern[0] 으로 뺌
# words 돌며 동일 절차 후 pattern 과 비교 

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        asciiPattern =''.join( [ord(i)-ord(pattern[0]) for i in pattern])
        return [i for i in words]