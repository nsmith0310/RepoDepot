class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        i = 0
        while i<len(equations):
            if "==" in equations[i]:
                tmp = equations[i].split("==")
                tmp.sort()
                if tmp[0]!=tmp[1]:
                    equations[i]='=='.join(tmp)
                else:
                    del equations[i]
                    i-=1
            else:
                tmp1 = equations[i].split("!=")
                tmp1.sort()
                if tmp1[0]!=tmp1[1]:
                    equations[i]='!='.join(tmp1)
                else:
                    return False
            i+=1
        
        l = list(set(equations))
       
        lim = len(l)
        if lim<=1:
            return True
        
        eq = dict()
        nonq = dict()
        
        i = 0
        while i<len(l):
            if "==" in l[i]:
                tmp = l[i].split("==")
                try:
                    eq[tmp[0]].append(tmp[1])
                except:
                    eq[tmp[0]] = [tmp[1]]
                try:
                    eq[tmp[1]].append(tmp[0])
                except:
                    eq[tmp[1]] = [tmp[0]]
                
            elif "!=" in l[i]:
                tmp = l[i].split("!=")
                try:
                    nonq[tmp[0]].append(tmp[1])
                except:
                    nonq[tmp[0]] = [tmp[1]]
                try:
                    nonq[tmp[1]].append(tmp[0])
                except:
                    nonq[tmp[1]] = [tmp[0]]
                    
            i+=1
        
        while 1!=-1:
            t = 0
            for x in eq:
                l2 = eq.get(x)
                for y in l2:
                    l3 = eq.get(y)
                    l4 = list(set(l2+l3))
                    
                    if len(l2)!=len(l4) or len(l3)!=len(l4):
                        
                        t = 1
                        eq[x]=l4
                        eq[y]=l4
            if t==0:
                break
                
        for x in nonq:
            l2 = nonq.get(x)
            for y in l2:
                try:
                    l4 = l2+eq[y]
                except:
                    pass
        
        for x in nonq:
            l2 = nonq.get(x)
            
            try:
                l3 = eq.get(x)
                    
                if len(l3+l2)!=len(list(set(l3+l2))):
                    
                    return False
            except:
                pass
        return True
            
        
        
        
        
                
        
            
        
