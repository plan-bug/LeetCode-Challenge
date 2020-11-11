class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        lst = []
        for i in range(len(arr)-1):
            lst.append([arr[i], arr[i+1], arr[i+1] - arr[i]])
        
        lst = sorted(lst, key=lambda x:x[2])
        
        answer = []
        for l in lst:
            if l[2] == lst[0][2]:
                answer.append([l[0], l[1]])
        
        return answer
