class Solution:
    def primes(self, n:int) -> int:
    
        sieve = [True] * n
        for i in range(3,int(n**0.5)+1,2):
            if sieve[i]:
                sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
        return [2] + [i for i in range(3,n,2) if sieve[i]]

    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        else:
            l = self.primes(n)
            if n in l:
                
                return len(l)-1
            else:
                return len(l)
        
