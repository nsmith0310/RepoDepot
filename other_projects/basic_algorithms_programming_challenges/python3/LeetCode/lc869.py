###powers of 2: the binary representation of the number, considered as base 10,
###i.e. 2^2 = 10 considered as 10
###0 = 0, 1 = 1, and all others are powers of 10

from itertools import permutations as p
from math import log
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        k = list(str(N))
        
        l = list(p(k))
        
        for x in l:
            if x[0]!='0':
                s = int(''.join(x))
                t = str(bin(s))[2:]
                
                k = len(t)
                ###print(t,k)
                if k==1:
                    if t=='1':
                        return True
                else:
                    if t[0]=="1" and int(t[1:])==0:
                        return True
            
            
        return False
        
        
        
