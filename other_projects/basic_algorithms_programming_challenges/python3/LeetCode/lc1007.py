class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        lim = len(A)
        
        a = [0 for i in range(0,6)]
        b = [0 for i in range(0,6)]
        c = [0 for i in range(0,6)]
        i = 1
        while i<=6:
            a[i-1]=A.count(i)
            b[i-1]=B.count(i)
            
                
            i+=1
            
        i = 0
        while i<lim:
            if A[i]==B[i]:
                c[A[i]-1]+=1
            i+=1
        
        
        mn = lim+1
        
        i = 0
        while i<len(a):
            if a[i]+b[i]-c[i]>=lim:
                
                if sum(a[:i]+a[i+1:])<mn: mn = sum(a[:i]+a[i+1:])
            i+=1
        i = 0
        while i<len(b):
            if a[i]+b[i]-c[i]>=lim:
                if sum(b[:i]+b[i+1:])<mn: mn = sum(b[:i]+b[i+1:])
            i+=1
        if mn!=lim+1:
            return mn
        else:
            return -1
            
