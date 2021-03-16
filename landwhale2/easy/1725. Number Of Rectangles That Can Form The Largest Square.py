class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        dict=defaultdict()
        ans=0
        
        for i,j in rectangles:
            mini=min(i,j)
            if mini not in dict:
                dict[mini]=1
            else:
                dict[mini]+=1
            ans=max(ans,mini)
        return dict[ans]
