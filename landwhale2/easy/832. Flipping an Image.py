class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            arr = A[i][::-1]
            for j in range(len(arr)):
                arr[j] = 1 - arr[j]
            A[i] = arr
        return A
