class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        return len([i for i in s[:len(s)//2] if i in vowels]) == len([i for i in s[len(s)//2:] if i in vowels])