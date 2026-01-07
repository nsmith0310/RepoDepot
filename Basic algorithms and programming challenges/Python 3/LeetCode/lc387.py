class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s=="":
            return -1
        s2 = list(set(s))
        l=[]
        l2=[]
        for x in s2:
            l.append([s.count(x),x])
        
        for x in l:
            if x[0]==1:
                l2.append(x)
        if l2==[]:
            return -1
                
        l3=[]
        for x in l2:
            l3.append(s.index(x[1]))
        return min(l3)
            
