# 논리

# 가장 큰

class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        ans = []
        while s:
            temp = list(set(s))
            temp.sort(key=lambda c: ord(c))
            for i in temp:
                ans.append(i)
                s.remove(i)
            temp = list(set(s))
            temp.sort(key=lambda c: ord(c), reverse=True)
            for i in temp:
                ans.append(i)
                s.remove(i)
        return ''.join(ans)


solution = Solution()
print(solution.sortString("aaawqeqwaabberqwedasfbbcccccddddeee"))
