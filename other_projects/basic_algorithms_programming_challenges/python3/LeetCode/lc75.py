class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if 1 in nums and 2 in nums and 0 in nums:
            m = 0
            p = 0
            i = 0
            while i<len(nums)-m:
                if nums[i]==0:
                    del nums[i]
                    nums.insert(0,0)
                elif nums[i]==2:
                    m+=1
                    del nums[i]
                    nums.append(2)
                    i-=1
                i+=1
        elif 0 in nums and 1 in nums:
            m = 0
            p = 0
            i = 0
            while i<len(nums):
                if nums[i]==0:
                    del nums[i]
                    nums.insert(0,0)
                
                i+=1
        elif 0 in nums and 2 in nums:
            m = 0
            p = 0
            i = 0
            while i<len(nums):
                if nums[i]==0:
                    del nums[i]
                    nums.insert(0,0)
                
                i+=1
        elif 1 in nums and 2 in nums:
            m = 0
            p = 0
            i = 0
            while i<len(nums):
                if nums[i]==1:
                    del nums[i]
                    nums.insert(0,1)
                
                i+=1
                    
            
        
                
                
