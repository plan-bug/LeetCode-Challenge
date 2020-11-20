# 새로운 list(스택) 생성

class Solution:
    def removeDuplicates(self, S: str) -> str:
        newList = []
        for letter in S:
            newList.append(letter)
            if len(newList) > 1 and newList[-1] == newList[-2]:
                newList.pop()
                newList.pop()

        return "".join(newList)


solution = Solution()
print(solution.removeDuplicates("abbaca"))
