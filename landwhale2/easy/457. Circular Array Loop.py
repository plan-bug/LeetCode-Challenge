class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 2:
            return False
        
        n = len(nums)
        for i in range(n):           
            if type(nums[i]) != int: # visited element
                continue
            if nums[i] % n == 0: # self-loop
                continue
            
            direction = (nums[i] > 0) # loop direction, cannot be changed midway
            
            mark = str(i)
            while (type(nums[i]) == int) and (direction ^ (nums[i] < 0)) and (nums[i] % n != 0):
                jump = nums[i]
                nums[i] = mark
                i = (i + jump) % n
                
            if nums[i] == mark:
                return True
            
        return False
