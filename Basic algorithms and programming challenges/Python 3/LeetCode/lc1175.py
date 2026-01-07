class Solution:
    def f(self, n: int) -> int:
        t = 1
        i = 2
        while i<=n:
            t*=i
            i+=1
        return t
        
    def numPrimeArrangements(self, n: int) -> int:
       
        primes = []
        
        if n==1:
            return 1
        if n==2:
            return 1
        
        for x in range(2,n+1):
            t=0
            for y in range(2,x):
                if x%y==0:
                    t=1
                    break
            if t==0:
                primes.append(x)
        
        return (self.f(len(primes))*self.f(n-len(primes)))%(10**9 + 7)
