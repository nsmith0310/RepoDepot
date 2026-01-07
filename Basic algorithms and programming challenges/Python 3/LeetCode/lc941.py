class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A)<=2:
            return False
        
        mx = max(A)
        
        ind = A.index(mx)
        if ind==0 or ind==len(A)-1:
            return False
        i = 0
        while i<ind:
            if A[i]>=A[i+1]:
                return False
            i+=1
        i = ind
        
        while i<len(A)-1:
            if A[i]<=A[i+1]:
                return False
            i+=1
        return True
