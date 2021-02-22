class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs==[]:
            return ''
        if len(strs)==1:
            return strs[0]
        l=len(strs[0])
        s=strs[0]
        for i in strs:
            if len(i)<l:
                l=len(i)
                s=i
        for i in range(l,0,-1):
            for j in strs:
                if j[:i]!=s[:i]:
                    break
            else:
                return s[:i]
        return ''
