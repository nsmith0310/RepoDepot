class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        k = (set(nums))
            
        return list(set([i for i in range(1,len(nums)+1)])-k)
