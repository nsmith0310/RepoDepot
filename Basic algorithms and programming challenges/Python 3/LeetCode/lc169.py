class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)//2
        l2 = list(set(nums))
        nums.sort()
        for x in l2:
            if nums.count(x)>l:
                return x
            
