class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        result = ''
        while s:
            arr = sorted(list(set(s)))
            result += ''.join(arr)
            
            for st in arr:
                s.remove(st)
            
            arr = sorted(list(set(s)), reverse=True)
            result += ''.join(arr)
            
            for st in arr:
                s.remove(st)
        return result
