class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
     
        lim = len(A)
        if lim<=1:return 0
        
        c = 0
        
        i = 0
        while i<len(A)-1:
            ###print(A)
            if A[i]==A[i+1]:
                c+=1
                A[i+1]+=1
            elif A[i]>A[i+1]:
                c+=A[i]-A[i+1]+1
                A[i+1]+=A[i]-A[i+1]+1
            i+=1
        ###print(A)
        return c
