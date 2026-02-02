class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        
        lim = len(A)
        
        
        tmp = [[B[i],i] for i in range(0,lim)]
        tmp.sort(key=lambda x: x[0])
        A.sort()
        lim2=lim
        i = 0
        while i<len(tmp):
            j = 0
            while j<len(A) and A[j]<=tmp[i][0]:
                j+=1
            if j==lim:
                tmp[i][0]=A[0]
                lim-=1
                del A[0]
            else:
                ###print(j,tmp,A)
                tmp[i][0]=A[j]
                lim-=1
                del A[j]
            i+=1
        tmp.sort(key=lambda x: x[1])
        f = [tmp[i][0] for i in range(0,lim2)]
        return f
            
