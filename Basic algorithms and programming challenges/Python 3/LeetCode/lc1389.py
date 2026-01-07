class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        t = []
        i = 0
        while i<len(nums):
            t.insert(index[i],nums[i])
            i+=1
        return t
