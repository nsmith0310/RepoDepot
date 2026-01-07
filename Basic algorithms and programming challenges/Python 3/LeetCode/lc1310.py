class Solution:
    
    
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        lim = len(arr)
        
        b = dict()
        f = dict()

        t = 0
        
        i = 0
        while i<lim:
            t^=arr[i]
            b[i]=t
            
            i+=1
        t2 = 0  
        i = 0
        while i<lim:
            t2^=arr[i]
            f[i+1]=t^t2
            i+=1
        
        
        r = []
        
        for x in queries:
            
            if x[0]-1>=0 and x[1]+1<lim:
                
                r.append((t^b[x[0]-1])^f[x[1]+1])
                
            elif x[0]-1>=0:
                r.append(t^b[x[0]-1])
            elif x[1]+1<lim:
                
                r.append(t^f[x[1]+1])
            else:
                r.append(t)
        return r
