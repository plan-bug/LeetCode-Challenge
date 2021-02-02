class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        words = list(map(set, words))
        result = 0
        for word in words:
            for s in word:
                if s not in list(allowed):
                    result += 1
                    break
        
        return len(words) - result
