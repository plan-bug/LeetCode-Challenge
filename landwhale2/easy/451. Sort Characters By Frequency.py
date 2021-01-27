class Solution:
    def frequencySort(self, s: str) -> str:
        dic = dict()
        for z in s:
            try:
                dic[z] += 1
            except:
                dic[z] = 1
        
        res = sorted(dic.items(), key=(lambda x:x[1]), reverse=True)

        result = ''
        for key,value in res:
            result += (key * value)
        
        return result
