class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
            
        lim = len(nums)
        
        if lim<=1 or k==0:
            return True
        c=0
        i = 0
        while i<lim-1:
            if nums[i+1]==1:
                
                if c<k:
                    if not(nums[i]==0 and nums[i+1]==1 and i==0):
                        
                        return False
                c=0
            else:
                c+=1
            i+=1
        return True
