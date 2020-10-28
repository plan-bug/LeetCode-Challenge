class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ret, counter = 0, collections.Counter(chars)
        for word in words:
            c = collections.Counter(word)
            if all(c[i] <= counter[i] for i in word):
                ret += len(word)
        return ret
