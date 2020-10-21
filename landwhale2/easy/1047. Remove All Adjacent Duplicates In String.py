class Solution:
    def removeDuplicates(self, S: str) -> str:
        check = True
        S = list(S)
        while check:
            check = False
            for i in range(len(S)-1):
                if S[i] == S[i+1]:
                    S.pop(i)
                    S.pop(i)
                    check = True
                    break
        
        return ''.join(S)
