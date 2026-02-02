class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        
        f = []
        l = []
        i = 0
        while i<len(A):
            if A[i]&1==False:
                f.append(A[i])
            else:
                f.append(0)
            i+=1
        
        for x in queries:
            if (A[x[1]]+x[0])&1==False:
                f[x[1]]=(A[x[1]]+x[0])
            else:
                f[x[1]]=0
            A[x[1]]+=x[0]
            l.append(sum(f))
        return l
