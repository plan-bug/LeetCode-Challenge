class Solution :
    def countConsistentStrings(self, allowed, words):
        return sum(all(c in allowed for c in w)for w in words)