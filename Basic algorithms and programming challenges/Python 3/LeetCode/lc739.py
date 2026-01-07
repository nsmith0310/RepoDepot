class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        ind = [[] for x in range(0,71)]
        
        i = 0
        while i<len(T):
            ind[T[i]-30].append(i)
            i+=1
        '''
        i = 0
        while i<len(ind):
            
            print(i+30,ind[i][:4])
            i+=1
        '''
        lim = len(ind)
        f=[]
        i = 0
        while i<len(T):
            
            j = T[i]-30 + 1
            mx = 10**32
            pos=-1
            while j<lim:
                if ind[j]!=[] and ind[j][0]>i:
                    if ind[j][0]<mx:
                        mx = ind[j][0]
                        pos = j
                j+=1
            
            if j==lim and pos==-1:
                f.append(0)
                
            else:
                f.append(mx-i)
                
            del ind[T[i]-30][0]
            i+=1
        
        return f
                
            
