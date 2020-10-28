# 논리

# 가장 큰

class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        temp = list(set(s))
        return temp


solution = Solution()
print(solution.sortString("aaawqeqwaabberqwedasfbbcccccddddeee"))
