class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        arr = [i for i in range(len(S)+1)]
        result = []
        for s in S:
            if s == 'I':
                arr = sorted(arr)
                result += arr[0:1]
                arr = arr[1:]
            else:
                arr = sorted(arr, reverse=True)
                result += arr[0:1]
                arr = arr[1:]
        
        return result + arr
