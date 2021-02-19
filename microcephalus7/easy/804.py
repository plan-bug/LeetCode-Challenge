class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
    	M = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
    	return len(set([''.join(map(lambda x: M[ord(x)-97], w)) for w in words]))