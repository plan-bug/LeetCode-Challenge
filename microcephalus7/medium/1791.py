# dict 구조 활용
# edges 각 요소 돌며 각 요소 값을 key 로 두고 counting
# dict 돌며 key value 가 edges 의 길이와 같은 key return  




class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dict = defaultdict(int)
        for i in edges:
            for j in i:
                dict[j]+=1
        for i,j in dict.items():
            if j == len(edges):
                return i