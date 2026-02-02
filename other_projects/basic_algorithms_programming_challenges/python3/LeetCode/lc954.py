class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort()
        i = 0
        while i<len(A)//2:
            if A[i]<=0:
                try: 
                    if A[i]%2==0:
                        ind = A.index(A[i]//2)
                        del A[ind]
                        del A[i]
                    else:
                        return False
                
                except:
                    
                    return False
            else:
                try: 
                    ind = A.index(A[i]*2)
                    del A[ind]
                    del A[i]
                
                except:
                    
                    return False
           
        return True
