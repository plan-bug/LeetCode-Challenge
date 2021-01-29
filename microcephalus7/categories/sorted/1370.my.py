# 논리

# 가장 큰

class Solution:
    def sortString(self, s: str) -> str:
        return list(set(list(s)))


solution = Solution()
print(solution.sortString("aaawqeqwaabberqwedasfbbcccccddddeee"))
