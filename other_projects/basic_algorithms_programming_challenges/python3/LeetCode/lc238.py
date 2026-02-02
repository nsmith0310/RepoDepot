class Solution:
    
   
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        t2 = [0 for i in range(0,len(nums))]
        t3 = [0 for i in range(0,len(nums))]
        lim = 10**32 - 1
        
        i = 0
        while i<len(nums):
            if t2[i]!=lim:
                t = 1
            
                l = 0
                r = i+1
                while l<i:
                    t*=nums[l]
                    l+=1
                while r<len(nums):
                    t*=nums[r]
                    r+=1
                
                t2[i]=t
                ind = nums[i]
                t2[i]=lim
                j = i
                while j<len(nums):
                    if nums[j]==ind:
                        t3[j]=t
                        t2[j]=lim
                    j+=1
                
            
            
            
            i+=1
        return t3
    
    
