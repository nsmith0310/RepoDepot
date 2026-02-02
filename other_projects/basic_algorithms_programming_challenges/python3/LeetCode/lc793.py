class Solution:
    def count(self,n):
        f = []
        i = 0
        while pow(5,i)<=n:
            x = n//pow(5,i)
            
            f.append(x)
            i+=1
        return sum(f[1:])
    def preimageSizeFZF(self, K: int) -> int:
        
        
        if K==0:
            return 5
        
        l = 1
        h = 10**10
        while l<=h:
            m = (l+h)//2
            num = self.count(m)
           
            if num>K-1:
                h = m-1
            else:
                l = m+1
        
        low = 0
        f = [l,h]
        f.sort()
        if self.count(f[1])==K-1:
            low = f[1]
        else:
            low = f[0]
            
        l = 1
        h = 10**10
        while l<=h:
            m = (l+h)//2
            num = self.count(m)
           
            if num>=K+1:
                h = m-1
            else:
                l = m+1
        
        high = 0
        f = [l,h]
        f.sort()
        if self.count(f[0])==K+1:
            high = f[0]
        else:
            high = f[1]
        
            
        return high-low-1
        
        
