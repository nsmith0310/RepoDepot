class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        l = list(s)
        
        l2 = []
        l3 = []
        
        i = 0
        while i<len(s):
            if s[i]=="(" or s[i]==")":
                l2.append(s[i])
                l3.append(i)
            i+=1
        
        
        
        
        while 1!=-1:
            t = 0
            i = 0
            while i<len(l2)-1:
                if l2[i] == "(" and l2[i+1]==")":
                    t = 1
                    del l2[i]
                    del l2[i]
                    del l3[i]
                    del l3[i]
                i+=1
            if t==0:
                break
                    
        c = 0
        for x in l3:
            del l[x-c]
            c+=1
        return ''.join(l)
            
            
            
        
        
        
        
                
