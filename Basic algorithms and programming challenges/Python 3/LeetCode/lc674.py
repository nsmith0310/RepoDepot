class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums==[]:return 0
        if len(nums)==1:return 1
        
        mx = 1
        i = 0
        
        
        c=1
        while i<len(nums)-1:
            if nums[i]<nums[i+1]:
                c+=1
                if c>mx:mx=c
            else:
                c=1
            i+=1
        return mx
