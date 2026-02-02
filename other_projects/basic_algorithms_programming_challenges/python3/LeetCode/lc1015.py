from math import gcd
class Solution:
    def p(self,a,n,m):
        if m==1:
            return 0
        r = 1
        b = a%m
        while n>0:
            if n %2 ==1:
                r = (r*b)%(9*m)
            n =n >> 1
            b=(b**2)%(9*m)
        return r
    def repunit(self,n):
        return (pow(10,n)-1)//9
    def smallestRepunitDivByK(self, K: int) -> int:
        if K%2==0 or gcd(K,10)!=1:return -1
        
        if K<100:
            
            i = 1
            while self.repunit(i)%K!=0:
                i+=1
            return len(str(self.repunit(i)))
        
        i = 1
        while self.p(10,i,K)!=1:
            i+=1
        
        return len(str(self.repunit(i)))
        
        
        
