# 아나그램 만들기
# 아냐그램이 뭐냐?
# 두 글자의 차이가 뭐냐
# 차이를 어떻게 이용할거냐

# s 의 각 알파벳 수와 t 의 각 알파벳 수의 차이를 비교
# defaultdict 이용
# s의 각 알파벳 수 dict 생성
# t 돌며 s 알파벳 수 하나씩 마이너스
# 남은 수 합쳐서 return



class Solution:
    def minSteps(self, s: str, t: str) -> int:
        memo = defaultdict(int)
        for i in s :
            memo[i] +=1
        for i in t:
            if memo[i]:
                memo[i]-=1
        return sum(memo.values())