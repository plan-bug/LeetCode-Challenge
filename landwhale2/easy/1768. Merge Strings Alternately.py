class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        result = ""
        while (len(word1) + len(word2)) != 0:
            if len(word1) != 0:
                result += word1.pop(0)
            
            if len(word2) != 0:
                result += word2.pop(0)
        
        return result
