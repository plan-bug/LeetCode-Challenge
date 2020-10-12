class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        arr = []
        left, right = 0,0
        tmp = ''
        for s in S:
            if s == '(':
                left += 1
            else:
                right += 1
            
            tmp += s
            
            if left == right:
                arr.append(tmp)
                tmp = ''
        
        result = ''
        for s in arr:
            result += s[1:-1]
        
        return result
