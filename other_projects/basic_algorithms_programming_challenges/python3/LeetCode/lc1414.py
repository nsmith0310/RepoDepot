
class Solution:
        
    def findMinFibonacciNumbers(self, k: int) -> int:
        l = [1,1]
        lim = 2
        while l[-1]+l[-2]<=k:
            l.append(l[-1]+l[-2])
            lim+=1
        
        l = l[::-1]
        mn = lim+1
        c=0
        for x in l:
            if k-x>=0:
                c+=1
                k-=x
        return c
