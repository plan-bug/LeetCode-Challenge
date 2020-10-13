class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alpha = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        arr = []
        for word in words:
            w = ''
            for s in word:
                w += alpha[ord(s) - 97]
            arr.append(w)
        
        return len(list(set(arr)))
