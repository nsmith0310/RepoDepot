class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A)<3:
            return 0
        mx = 0
        
        p = 0
        
        A.append(10**9)
        A.append(10**9)
        c = 0
        i = 0
        while i<len(A)-1:
            if p==0 and A[i]<A[i+1]:
                c+=1
            elif p==0 and c>0 and A[i]>A[i+1] and A[i]!=A[i-1]:
                
                c+=1
                p = 1
            elif p==0 and c>0 and A[i]>A[i+1] and A[i]==A[i-1]:
                c=0
            elif p==1 and A[i]>A[i+1]:
                c+=1
            elif p==1 and A[i]<A[i+1]:
                c+=1
                
                if c>mx:
                   
                    mx = c
                p = 0
                
                c = 1
            i+=1
        
        if mx>0:
            return mx
        else:
            return 0
                
