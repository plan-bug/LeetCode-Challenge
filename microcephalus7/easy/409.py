# 필요 조건
# 회문구조란? : 앞/뒤로 읽어도 같은 구조
# 회문구조문의 특징 : 글자 수가 홀수/짝수일 경우 가운데는 하나/둘,
# 글자수가 홀수 일경우 중간에 하나만 가능함

# 숙지사항
# 회문구조문이 아닌 회문구조문이 될 수 있는 최고 길이를 말함
# 즉 회문구조문을 짤 필요 없이 조건에 맞게 최대인 숫자만 return 하면 됨

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        oneCount = 0
        res = 0

        for i in counter:
            if counter[i] % 2 == 1 and oneCount == 0:

                res += 1
                oneCount += 1
                counter[i] -= 1

            rem = counter[i] // 2
            res += 2 * rem
            counter[i] -= rem * 2

        return res


sol = Solution()
print(sol.longestPalindrome("abccccdd"))
