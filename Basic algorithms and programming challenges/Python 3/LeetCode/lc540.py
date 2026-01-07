class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[-2]!=nums[-1]:
            return nums[-1]
        
        i = 0
        while i<len(nums)-1:
            b = nums[i]
            f = nums[i+1]
            if b==f:         
                i+=2
            else:
                return b
            
