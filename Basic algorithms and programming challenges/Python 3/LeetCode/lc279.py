from copy import copy


class Solution:
    
    def s(self,i):
        f = []
        t = set()
        while i%2==0:
            f.append(2)
            t.add(2)
            i//=2
        for j in range(3,int(i**.5)+1,2):
            while i%j==0:
                f.append(j)
                t.add(j)
                i//=j
        if i>2:
            f.append(i)
            t.add(i)
            
        for x in t:
            if x%4==3 and f.count(x)%2!=0: return False
        return True
        
    def numSquares(self, n: int) -> int:
        
        nums = []
        pos = []
        c=0
        i = 1
        while i**2<=n:
            nums.append(i**2)
            i+=1
            
        mn = 5
        
        for x in nums:
            if n%x==0:
                if n//x<=4:
                    pos.append(n//x)
                    c+=1
        if c>0:
            pos.sort()
            mn = pos[0]
            if mn==1:return 1
            elif mn==2: return 2
        check = 0
        nums.sort(reverse=True)
        
        tmp2 = []
        for x in nums:
            if (n-x) in nums: 
                return 2
            else:
                if self.s(n-x)==True:
                    
                    check=1
                
           
            
        if 3 in pos or check==1:
            return 3
        return 4
            
        
        
    
        
        
