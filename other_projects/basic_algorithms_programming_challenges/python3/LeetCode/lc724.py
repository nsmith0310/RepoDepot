class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)<2:
            return -1
        
        i = 0
        while i<len(nums):
            ###print(i,sum(nums[:i]),sum(nums[i+1:]))
            if sum(nums[:i])==sum(nums[i+1:]):
                return i
            i+=1
        return -1
