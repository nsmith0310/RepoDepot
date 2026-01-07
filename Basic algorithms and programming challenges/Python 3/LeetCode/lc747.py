class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        num = max(nums)
        ind = nums.index(num)
        del nums[ind]
        i = 0
        while i<len(nums):
            if 2*nums[i]>num:
                return -1
            i+=1
        return ind
