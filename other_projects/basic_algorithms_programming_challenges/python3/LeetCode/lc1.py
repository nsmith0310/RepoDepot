class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in nums:
            
            if target-x in nums:
                if nums.index(x)!=nums.index(target-x):
                    return [nums.index(x),nums.index(target-x)]
                elif nums.index(x)==nums.index(target-x) and nums.count(x)>1:
                    i = nums.index(x)+1
                    while i<len(nums):
                        if x==nums[i]:
                            return [nums.index(x),i]
                        i+=1
            
        return "no two list elements sum to " + str(target)
            
            
