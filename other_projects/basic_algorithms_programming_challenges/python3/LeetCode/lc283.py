class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        b = nums.count(0)
        
        v = 0
        i = 0
        while i<len(nums):
            if nums[i]==0:
                
                
                del nums[i]
                nums.append(0)
                v+=1
                if v==b:
                    break
                i-=1
                
            i+=1
        
