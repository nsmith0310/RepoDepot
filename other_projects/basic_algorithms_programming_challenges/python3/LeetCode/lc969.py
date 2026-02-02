class Solution:
    
    def r(self,A,i):
        A[:i+1]=A[:i+1][::-1]
        return A
    def mx(self,A,i):
        m = -99999999999999
        mi = 0
        j = 0
        while j<i:
            if A[j]>m:
                m = A[j]
                mi = j
            j+=1
        return mi
        
    def pancakeSort(self, A: List[int]) -> List[int]:
        
        f = []
        lim = len(A)
        
        while lim>1:
            ind = self.mx(A,lim)
            A = self.r(A,ind)
            f.append(ind+1)
            f.append(lim)
            A = self.r(A,lim-1)
            lim-=1
        return f
