# 아나그램 만들기
# s 의 각 알파벳 수와 t 의 각 알파벳 수의 차이를 비교



class Solution:
    def minSteps(self, s: str, t: str) -> int:
        memo = defaultdict(int)
        for i in s :
            memo[i] +=1
        for i in t:
            if memo[i]:
                memo[i]-=1
        return sum(memo.values())