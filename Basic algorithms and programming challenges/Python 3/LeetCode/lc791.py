class Solution:
    def customSortString(self, S: str, T: str) -> str:
        l = [[x,S.index(x),T.count(x)] for x in S]
        l.sort(key=lambda x: x[1])
        
        l2 = []
        i = 0
        while i<len(T):
            if T[i] not in S:
                l2.append(T[i])
            i+=1
        app = ''.join(l2)
        
        s=""
        for x in l:
            if x[2]!=0:
                i = 0
                while i<x[2]:
                    s+=x[0]
                    i+=1
        s+=app
        return s
        
        
