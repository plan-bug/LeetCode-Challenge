class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        result = []
        for a in arr1:
            try: dic[a] += 1
            except: dic[a] = 1

        for a in arr2:
            for _ in range(dic[a]):
                dic[a] -= 1
                result.append(a)

        for a in sorted(arr1):
            if dic[a] > 0:
                result.append(a)
                dic[a] -= 1
        return result
