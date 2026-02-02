class Solution:
    def fib(self, N: int) -> int:
        l=[0,1]
        if N==0:
            return 0
        elif N==1:
            return 1
        
        i = 2
        while i<=N:
            l.append(l[-1]+l[-2])
            i+=1
        return l[-1]
            
