class Solution:
    def freqAlphabets(self, s: str) -> str:
        node = len(s) - 1
        result = ''
        while node >= 0:
            if s[node] == '#':
                result += chr(int(s[node-2:node]) + 96)
                node -= 3
            else:
                result += chr(int(s[node]) + 96)
                node -= 1
        
        return result[::-1]
