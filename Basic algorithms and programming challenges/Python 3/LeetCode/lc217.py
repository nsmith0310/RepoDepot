class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = len(nums)
        b = len(list(set(nums)))
        return b<a
