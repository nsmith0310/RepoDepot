from math import ceil
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        lim = len(seats)
        
        b0 = 0
        f0 = 0
        
        a = 0
        b = 0
        
        g_max = 0
        l_max = 0
        
        i = 0
        
        while i<lim:
            if i==lim-1:
                if seats[i]==1:
                    if b==0:
                        if i+1>g_max:
                            g_max=i
                else:
                    if l_max+1>g_max:
                        g_max = l_max+1
            if seats[i]==0:
                a = i
                l_max+=1
            else:
                if l_max%2==0:
                    if b==0:
                        num = l_max
                    else:
                        num = l_max//2
                else:
                    if b==0:
                        num = l_max
                    else:
                        num = ceil(l_max/2)
                if num>g_max:
                    g_max = num
                    b0 = b
                    f0 = i
                l_max=0
                b = i+1                
            i+=1
        return g_max
            

        
