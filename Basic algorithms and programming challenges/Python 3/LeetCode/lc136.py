class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        t = 0
        p = 0
        while i<len(nums):
            if p==0:
                t+=nums[i]
                p=1
                
            elif p==1:
                t-=nums[i]
                p = 0
                
            
            i+=1
        return t
