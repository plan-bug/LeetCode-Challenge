class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        ops = cnt = 0 # count of remaining "1"s
        for i, x in enumerate(boxes):
            if x == "1": 
                ops += i
                cnt += 1
        
        for i, x in enumerate(boxes): 
            ans.append(ops)
            if x == "1": cnt -= 2
            ops -= cnt
        return ans 