class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = dict()
        for n in arr:
            try:
                count[n] += 1
            except:
                count[n] = 1
        arr = []
        for v in count.values():
            arr.append(v)
        
        return len(arr) == len(list(set(arr)))
