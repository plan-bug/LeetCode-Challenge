# counter
# inner ( 와 outter ) 수가 같아지면 그 시점에서 string 자르고 첫번째와 마지막 string 에 추가

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        newIndex = 0
        string = ""
        for i in range(len(S)):
            if S[i] == "(":
                count += 1
            else:
                count -= 1
            if count == 0:
                string += S[newIndex+1:i]
                newIndex = i+1
        return string


solution = Solution()
print(solution.removeOuterParentheses("(()())(())"))
