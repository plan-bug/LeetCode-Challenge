class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        if A and not B:
            return -1
        if not A and B:
            return -1
        if not A and not B:
            return -1
        
        if len(A) != len(B):
            return -1

        return_val = -1
        for val in [A[0], B[0]]:            
            num_a = 0
            num_b = 0
            for ind,(a,b) in enumerate(zip(A,B)):

                if a == val:
                    num_a += 1
                if b == val:
                    num_b += 1

                if a != val and b != val:
                    break
        
                if ind == len(A) -1:
                    if return_val == -1:
                        return_val = min(len(A)-num_a, len(A)-num_b)
                    else:
                        return_val = min(return_val, min(len(A)-num_a, len(A)-num_b))
                
        return return_val
