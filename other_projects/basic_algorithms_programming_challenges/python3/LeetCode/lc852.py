class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        i = 0
        m = max(A)
        j = A.index(m)
        while i<len(A)-1:
            if A[i]>=A[i+1] and i<j:
                
                return None
            if A[i]<=A[i+1] and i>j:
                return None
            i+=1
        
        return j
