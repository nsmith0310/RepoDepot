from copy import copy

class Solution:
    
                
                
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        lim = len(nums)
        tmp = [[[nums[i]],i] for i in range(0,lim)]
        
        ###print(tmp)
        f = []
        
        val = 0
        
        tmp3 = [x for x in nums]
        
        if len(list(set(tmp3)))==len(nums):
            
            val =1
            
        for x in tmp:
            z = copy(x)
            i = x[1]+1
            while i<lim:
                if nums[i]>=z[0][-1]:
                    tmp2 = z[0]+[nums[i]]
                    
                    f.append(tmp2)
                    tmp.append([tmp2,i])
                    
                i+=1
        if val==0:
            f2=[]
            for x in f:
                if x not in f2:
                    f2.append(x)
            return f2
        else:
            return f
        
        
        
        
        
        
                    
                
