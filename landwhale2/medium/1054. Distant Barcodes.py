class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        heap = []
        l = []
        c = Counter(barcodes)
        for x in c: #push negetive counts since we will push the smallest 
            heappush(heap,(-c[x],x))
    
        while(heap):
            first = heappop(heap) #always pop the number with the largest number of "stocks"
            if first[0]==0:
                return l
            elif not l or first[1]!=l[-1]: #check if the current number is same as the last one in l
                l.append(first[1])
                heappush(heap,(first[0]+1,first[1]))
            else:
                second = heappop(heap)
                l.append(second[1])
                heappush(heap,first)
                heappush(heap,(second[0]+1,second[1]))
        
