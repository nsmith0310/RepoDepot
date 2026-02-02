class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        lim = len(satisfaction)
        
        t = 0
        mx = max(satisfaction)
        mn = min(satisfaction)
        
        
        
        if mx<=0:return 0
        
        if mn>0:
            satisfaction.sort()
            
            i = 0
            while i<lim:
                t+=(i+1)*satisfaction[i]
                i+=1
            return t
        
        satisfaction.sort()
        l = [i for i in range(1,lim+1)]
        
        mx = 0
        i = 0
        while i<lim:
            
            mx+=satisfaction[i]*l[i]
            i+=1
        
        
        while 1!=-1 and lim>0:
            
            tmp = 0
            del satisfaction[0]
            del l[0]
            lim-=1
            i = 0
            while i<lim:
                l[i]-=1
                i+=1
            i = 0
            while i<lim:
                tmp+=satisfaction[i]*l[i]
                i+=1
            
            if tmp>mx:
                mx = tmp
            else:
                return mx
        
        
        return mx
        
        
        
        
               
        
        
                
