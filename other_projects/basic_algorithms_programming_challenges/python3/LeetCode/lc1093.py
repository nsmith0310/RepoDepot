from math import ceil

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        
        f = [0,0,0,0,0]
        
        med = sum(count)
        
        c = 0
        if med&1==True:
            i = 0
            while i<len(count):
                c+=count[i]
                if c>=ceil(med/2):
                    f[3]=i
                    break
                
                i+=1
        else:
            i = 0
            while i<len(count):
                c+=count[i]
                if c>med//2:
                    f[3]=i
                    break
                elif c==med//2:
                    
                    f[3] = (2*i + 1)/2
                    break
                i+=1
    
        mn = 256
        mx = 0
        
        meannum = 0
        meanden = 0
        
        i = 0
        while i<len(count):
            if count[i]>0 and i>mx:mx = i
            if count[i]>0 and i<mn:mn = i
            meannum+=count[i]*i
            meanden+=count[i]
            i+=1
        f[0]=mn
        f[1]=mx
        f[2]=meannum/meanden
        f[4]=count.index(max(count))
        return f
            
