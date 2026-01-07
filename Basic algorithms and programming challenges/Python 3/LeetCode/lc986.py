class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        c1= 0 
        c2 = 0
        f = []
        l = []
        for x in A:
            l.append(x+['A'])
            c1+=1
        for x in B:
            l.append(x+['B'])
            c2+=1
        if c1==0 or c2==0: return []
        if c1+c2<2:
            return []
        
        l.sort(key=lambda x: x[0])
        ###print(l)
        lim = len(l)
        i = 0
        while i<lim-1:
            if l[i][1]>=l[i+1][0] and l[i][2]!=l[i+1][2]:
                f.append([l[i+1][0],min([l[i+1][1], l[i][1]])])
                        
                if i<lim-2 and l[i+1][2]==l[i+2][2]:
                    l[i+1]=l[i]
                    
                          
                
            i+=1
        return f
                
