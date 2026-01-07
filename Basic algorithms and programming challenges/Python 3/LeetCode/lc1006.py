class Solution:
    def clumsy(self, N: int) -> int:
        if N==0:
            return 0
        if N==1:
            return 1
        ops = ["*","/","+","-"]
        nums = [x for x in range(N,0,-1)]
        l = []
        c=0
        for x in nums:
            if c == 4: c=0
            l.append(x)
            l.append(ops[c])
            c+=1
        del l[-1]
        
        tmp = 0
        i = 0
        while i<len(l):
            if l[i]=="*":
                tmp = l[i-1]*l[i+1]
                del l[i-1]
                l[i-1] = tmp
                
                del l[i]
            i+=1
        
        tmp = 0
        i = 0
        while i<len(l):
            if l[i]=="/":
                tmp = l[i-1]//l[i+1]
                del l[i-1]
                l[i-1] = tmp
                
                del l[i]
            i+=1
        t = l[0]
        i = 0
        while i<len(l):
            if l[i]=="+":
                t+=l[i+1]
            elif l[i]=='-':
                t-=l[i+1]
            i+=1
            
        return t
