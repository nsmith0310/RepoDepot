class Solution:
    def printVertically(self, s: str) -> List[str]:
        l = s.split(" ")
        mx =  0
        l2 = []
        for x in l:
            if len(x)+1>mx:
                mx = len(x)+1
            l2.append(x+" ")
        
        
        l3 = ['' for i in range(0,mx)]
        print(l)
        print(l2)
        print(l3)
        i = 0
        while i<len(l2):
            j = 0
            while j<len(l3):
                if j<len(l2[i]):
                    l3[j]+=l2[i][j]
                else:
                    l3[j]+=' '
                j+=1
            i+=1
            
        del l3[-1]
        final = []
        for x in l3:
            k = len(x)-1
            while x[k]==' ':
                k-=1
            final.append(x[:k+1])
        return final
            
        print(l3)
                    
                
                
            
                
