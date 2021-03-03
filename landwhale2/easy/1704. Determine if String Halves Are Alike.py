class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        string = "aeiouAEIOU"
        vowels = set(string)
        c = 0
        for i in range(len(s)//2):
            if s[i] in vowels:
                c+=1
        for i in range(len(s)//2, len(s)):
            if s[i] in vowels:
                c-=1
        return c==0
