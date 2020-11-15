# defalultdict 로 유사 딕셔너리
# list 이터레이션
# 공백 기준으로 나눔
# 점 기준으로 나눔
# 점 기준으로 나눈 길이 0 될떼 (while)까지 이름 앞의 1씩 자르며 누적
# 유사 딕셔너리 list로 return

from typing import List
from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain = defaultdict(int)
        for i in cpdomains:
            num, web = i.split(' ')
            web = web.split('.')
            while len(web) > 0:
                webName = '.'.join(web)
                web = web[1:]
                domain[webName] += int(num)
        return [str(count)+' '+web for web, count in domain.items()]
