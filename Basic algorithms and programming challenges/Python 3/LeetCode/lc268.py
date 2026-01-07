class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i<len(nums)-1:
            if nums[i]<nums[i+1]-1:
                return nums[i]+1
            i+=1
        if nums[0]==1:
            return 0
        else:
            return nums[-1]+1
