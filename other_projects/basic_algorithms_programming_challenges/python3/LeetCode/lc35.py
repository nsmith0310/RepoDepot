class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if target>=nums[-1]:
            return len(nums)
        if target<=nums[0]:
            return 0
        i = 0
        while nums[i]<=target:
            i+=1
        return i
