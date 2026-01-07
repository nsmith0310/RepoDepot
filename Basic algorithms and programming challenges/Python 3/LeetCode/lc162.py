class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lim = len(nums)
        if lim==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return lim-1
        
        i = 1
        while i<lim-1:
            if nums[i-1]<nums[i]>nums[i+1]:
                return i
            i+=1
        
        
