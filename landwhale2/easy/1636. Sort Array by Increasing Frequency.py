class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = dict()
        for n in nums:
            try:
                dic[n] += 1
            except:
                dic[n] = 1
        
        ar = sorted([k for k in dic.keys()], reverse=True)
        result = []
        arr = sorted(ar, key=lambda x: dic[x])
        for i in arr:
            for j in range(dic[i]):
                result.append(i)
        
        return result
