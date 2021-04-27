# 변수는 n
# FBS : 각 노드의 자식의 수가 0 아니면 2
# 노드 : 하나를 만들 때 마다 n에서 하나가 감소

class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n%2 == 0:
            return []
        memo = {}
        def do(n):
            if n == 1:
                return [TreeNode(0)]
            if n in memo:
                return memo[n]
            ways = []
            for i in range(1,n,2):
                left = do(i)
                right = do(n-i-1)
                ways.extend([TreeNode(0,l,r) for l in left for r in right])
            memo[n] = ways
            return ways
        return do(n)