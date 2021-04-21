class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer=[]
        for i in range(len(l)):
            temp=nums[l[i]:r[i]+1]
            temp.sort()
            x=temp[1]-temp[0]
            flag=0
            for j in range(2,len(temp)):
                if temp[j]-temp[j-1]!=x:
                    flag=1
                    break
            if flag==0:
                answer.append(True)
            else:
                answer.append(False)
        return answer