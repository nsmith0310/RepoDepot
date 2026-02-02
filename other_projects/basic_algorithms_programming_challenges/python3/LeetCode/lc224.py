class Solution:
    def calculate(self, s: str) -> int:
        
        
        
        l = s.split(" ")
        s = ''.join(l)
        i = 0
        
        
        s = list(s)
        i = 0
        while i<len(s):
            if s[i]=='0' and (s[i-1]=="+" or s[i-1]=="-"):
                del s[i]
                del s[i-1]
                i-=2
            i+=1
            
        
        
        
        i = 0
        
        while i<len(s):
            if s[i]==")":
                tmp = ""
                start = 0
                end = i
                j = i-1
                while j>=0:
                    if s[j]=="(":
                        start = j
                        break
                    tmp+=s[j]
                    
                    j-=1
                
                tmp = tmp[::-1]
                if tmp[0]!="-" and tmp[0]!="+":
                    tmp = "+"+tmp
                
                
                    
                ltmp = list(tmp)
                
                total = 0
                
                j = 0
                while j<len(ltmp):
                    if ltmp[j]=="+" or ltmp[j]=="-":
                        ltmp.insert(j,"n")
                        j+=2
                    else:
                        j+=1
                
                ltmp=''.join(ltmp)
                
                p = ltmp.split("n")
                
                if p[0]=='':
                    del p[0]
                j = 0
                
                while j<len(p):
                    if p[j][0]=="+":
                        if len(p[j])!=1:
                            total+=int(p[j][1:])
                    else:
                        if len(p[j])==1:
                            p[j+1]="-"+p[j+1]
                        else:
                            total-=int(p[j][1:])
                    j+=1
                
                tmp = list(str(total))
                
                s[start:end+1]=tmp
                i=start-1 
            i+=1
            
        num = ''.join(s)
        
        
        total = 0
        
        if num[0]!="+" and num[0]!="-":
            num = "+"+num
        l = list(num)    
        i = 0
        while i<len(l):
            if l[i]=="+" or l[i]=="-":
                l.insert(i,"n")
                i+=2
            else:
                i+=1
        
        
        l = ''.join(l)
        
        p = l.split("n")
        
        
        if p[0]=='':
            del p[0]
        j = 0
        
        while j<len(p):
            if p[j][0]=="+":
                if len(p[j])==1:
                    pass
                else:
                    total+=int(p[j][1:])
            else:
                if len(p[j])==1:
                    p[j+1] = "-"+p[j+1]
                else:
                    total-=int(p[j][1:])
            j+=1
            
        return str(total)
                
                    
