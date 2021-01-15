class Solution():
    def checkPossibility(self, nums):
        n = len(nums)
        if n<=2:
            return True
        
        count = 0
        check_sorted = 0
        
        for i in range(0,n-1):
            if nums[i] > nums[i+1]:
                count += 1
                if i != 0 and nums[i+1]<nums[i-1]:
                    nums[i+1] = nums[i]
            else:
                check_sorted += 1  
                
        if count == 1 or check_sorted == n-1:
            return True
        
        return False
