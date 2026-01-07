class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        lim = len(A)
        l = [[A[i],i] for i in range(0,lim)]
        
        l.sort(key=lambda x: x[0])
        
        mx = 0
        mn = 50001
        i = 0
        while i<lim:
            if l[i][1]-mn>mx:mx=l[i][1]-mn
            if l[i][1]<mn:mn = l[i][1]
            i+=1
        return mx
