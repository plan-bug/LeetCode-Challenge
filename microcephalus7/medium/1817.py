class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = defaultdict(set)
        for x,t in logs:
            d[x].add(t)
        ans = [0] * k
        for x in d:
            l = len(d[x])
            ans[l-1] +=1
        return ans