class Solution:
    def tar(self,l):
        
        l1 = list("abcde")
        if l in l1: return [0,l1.index(l)]
        
        l2 = list("fghij")
        if l in l2: return [1,l2.index(l)]
        
        l3 = list("klmno")
        if l in l3: return [2,l3.index(l)]
        
        l4 = list("pqrst")
        if l in l4: return [3,l4.index(l)]
        
        l5 = list("uvwxy")
        if l in l5: return [4,l5.index(l)]
        
        return [5,0]
        
        
        
    def alphabetBoardPath(self, target: str) -> str:
        l = list(target)
        f=""
        start = [0,0]
        
        while l!=[]:
            
            n = l[0]
            del l[0]
            t = self.tar(n)
            
            if start[0]<t[0]:
                if n!="z":
                    while start[0]<t[0]:
                        f+="D"
                        start[0]+=1
                else:
                    while start[0]<4:
                        f+="D"
                        start[0]+=1
                    
            elif start[0]>t[0]:
                
                while start[0]>t[0]:
                    f+="U"
                    start[0]-=1
                    
                    
            if start[1]<t[1]:
                
                while start[1]<t[1]:
                    f+="R"
                    start[1]+=1
            elif start[1]>t[1]:
                
                while start[1]>t[1]:
                    f+="L"
                    start[1]-=1
            if n=="z":
                if start[0]!=5:
                    f+="D"
                    start[0]+=1
            f+="!"
        return f
            
            
