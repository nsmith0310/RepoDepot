class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s = 1
        
        t = 1
        
        i = 0
        while i<len(nums):
            if nums[i]+s<1:
                t+= abs(s+nums[i])+1
                s = 1                
            else:
                s+=nums[i]
            i+=1
                
        return t
