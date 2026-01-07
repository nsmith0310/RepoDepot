class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        
        l = 1
        
        s = [A[0]]
        del A[0]
        
        mx = max(s)
        mn = min(A)
        
        while 1!=-1:
            ###print(s,A,mx,mn)
            
                
            if mx>mn:
                l+=1
                if A[0]>mx:
                    mx = A[0]
                if A[0]==mn:
                    s+=[A[0]]
                    del A[0]
                    mn = min(A)
                else:
                    s+=[A[0]]
                    del A[0]
            else:
                return l
                
