class Solution :
    def countConsistentStrings(self, allowed, words):
        return len([ [c in allowed for c in w] for w in words])