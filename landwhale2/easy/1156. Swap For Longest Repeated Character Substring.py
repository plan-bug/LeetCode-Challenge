from collections import defaultdict
from collections import Counter
class Solution:

    def maxRepOpt1(self, text: str) -> int:
        length = len(text)
        text += "!"
        d = defaultdict(list)
        c = Counter(text)
        start = [0,1]
        longtest = 0

        for i in range(length):
            if text[i] == text[i+1]:
                start[1]+=1
            else:
                longtest = max(longtest,start[1]+1) if start[1]<c[text[i]] else max(longtest,start[1])

                if d[text[i]] and d[text[i]][0]+d[text[i]][1]+1 == start[0]:
                    if d[text[i]][1] + start[1]<c[text[i]]:
                        longtest = max(longtest,d[text[i]][1] + start[1]+1)
                    else:
                        longtest = max(longtest,d[text[i]][1] + start[1])
                d[text[i]] = start.copy()
                start = [i+1,1]

        return longtest
