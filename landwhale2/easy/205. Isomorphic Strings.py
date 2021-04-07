class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_track = {}
        t_track = {}
        s_counter, t_counter = 0, 0
        
        for i in range(len(s)):
            if s[i] not in s_track:
                s_track[s[i]] = s_counter
                s_counter += 1
            
            if t[i] not in t_track:
                t_track[t[i]] = t_counter
                t_counter += 1
            
            if s_track[s[i]] != t_track[t[i]]:
                return False
        
        return True
