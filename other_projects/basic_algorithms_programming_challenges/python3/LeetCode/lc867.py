class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        r = len(A)
        c = len(A[0])
        
        m = [[] for i in range(1,c+1)]
        
        i = 0
        while i<len(A):
            j = 0
            while j<len(A[i]):
                m[j].append(A[i][j])
                j+=1
            i+=1
        return m
                
            
