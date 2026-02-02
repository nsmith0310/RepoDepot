class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        d = dict()
        
        for z in accounts:
            try:
                d[z[0]].append(z[1:])
            except:
                d[z[0]]=[z[1:]]
    
        f = []
        
        for x in d:
            
            lol = d.get(x)
            
            lim = len(lol)
            
            if lim==1:
                tmp3 = list(set(lol[0]))
                tmp3.sort()
                
                tmp3.insert(0,x)
                f.append(tmp3)
            else:
                kill = 0
                while 1!=-1:
                    kill=0
                    i = 0
                    while i<len(lol)-1:
                        j = i+1
                        while j<len(lol):
                        
                            tmp4a = list(set(lol[i]))
                            tmp4b = list(set(lol[j]))
                        
                        
                            tmp2 = tmp4a + tmp4b
                            if len(tmp2)!=len(list(set(tmp2))):
                                lol[i]=list(set(tmp2))
                                kill=1
                                del lol[j]
                                j-=1
                            
                            j+=1
                        i+=1
                    if kill==0:
                        break
                i = 0
                while i<len(lol):
                    tmp5 = list(set(lol[i]))
                    tmp5.sort()
                    f.append([x]+tmp5)
                    i+=1
        
        return f
                
                
                
