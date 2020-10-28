# 논리

# 중복 제거하고 정렬된 list 를 이용해 빼고 더함
# 역정렬해서 반복

class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        ans = []
        while s:
            # set 함수로 중복 제거
            temp = list(set(s))
            # 정렬 (ascii 코드값 기준)
            temp.sort(key=lambda c: ord(c))
            for i in temp:
                # 더하고 제거
                ans.append(i)
                s.remove(i)
            # 다시 중복 제거
            temp = list(set(s))
            # 거꾸로 정렬
            temp.sort(key=lambda c: ord(c), reverse=True)
            for i in temp:
                # 더하고 제거
                ans.append(i)
                s.remove(i)
        return ''.join(ans)


solution = Solution()
print(solution.sortString("aaawqeqwaabberqwedasfbbcccccddddeee"))
