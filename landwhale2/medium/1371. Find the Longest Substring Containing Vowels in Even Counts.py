class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        #strategy: Bitmask
        #d keeps track of first time the curr bitmask has been seen
        #convert means changing the char into the pos in the bitmask
        d, convert = {31 : -1}, {'a' : 0, 'e' : 1, 'i' : 2, 'o' : 3, 'u' : 4}
        
        answer, mask = 0, 31
        for i in range(len(s)):
            #update bitmask
            if s[i] in convert:
                mask ^= (1 << convert[s[i]])
            if mask in d:
                answer = max(answer, i - d[mask])
            #only update the pos the first time since we want the longest substr
            else:
                d[mask] = i
        return answer
