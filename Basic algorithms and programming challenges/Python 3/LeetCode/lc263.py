class Solution:
    def prime(self, n: int) -> int:
        f = []
        while n%2==0:
            f.append(2)
            n//=2
            
        
        for i in range(3,int(n**.5)+1,2):
            if n%i==0:
                while n%i==0:
                    f.append(i)
                    n//=i
        if n>2:
            f.append(n)
        return f
    def isUgly(self, num: int) -> bool:
        if num<1:
            return False
        if num==1:
            return True
        
        l = list(set(self.prime(num)))
        l.sort()
        print(l)
        if len(l)>0:
            if max(l)>5:
                return False
        return True
        
        
