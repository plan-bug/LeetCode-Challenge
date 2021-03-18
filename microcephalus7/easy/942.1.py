class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        return (lambda x : [x.pop() if i == "D" else x.popleft() for i in S]+[x[0]])(collections.deque(range(len(S)+1)))