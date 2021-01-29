# node 값들을 어떻게 분류하느냐

# 풀이
# collections 이용
# mv 를 변수로 두고 count 값 제일 큰 수 찾음
# mv 이용해서 compression

# 중요점
# collections 를 잘 활용함


import collections
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        counts = collections.Counter()
       
        def collector(node):
            
            if not node:
                return
            counts[node.val] +=1
            
            collector(node.left)
            collector(node.right)
        collector(root)
        countMax =  max([v for k,v in counts.items()])
        return [k for k,v in counts.items() if v == countMax]
        
        