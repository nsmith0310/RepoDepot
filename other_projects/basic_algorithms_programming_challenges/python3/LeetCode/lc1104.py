from math import log,floor

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        
        
        
        k = label
        
        l = [k]
        
        
        
        while k>1:
            if k%2==0:
                k//=2
                l.append(k)
            else:
                k = (k-1)//2
                l.append(k)
                
        l = l[::-1]
        if l[0]==0:
            del l[0]
                    
        lim = len(l)-1
        
        l2 = l[::-1]
        
        
        
        i = 0
        while i<len(l2):
            if i%2!=0:
                r = (floor(log(l2[i],2)))
                p = 2**r
                
            
                
                l2[i] = p + 2**(r+1) -l2[i]- 1
                
            i+=1
                
        return l2[::-1]
                
            
        
