class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        l = []
        for x in cpdomains:
            i = x.index(" ")
            count = int(x[:i+1])
            tmp = x[i:].split(".")
            tmp2 = []
            j = len(tmp)
            
            while j>=0:
                tmp3 = '.'.join(tmp[j:])
                if ' ' in tmp3:
                    tmp3=tmp3[1:]
                if tmp3!='':
                    l.append([count,tmp3])
                j-=1
            
                
        l.sort(key=lambda x: x[1])
        f = []
        
        i = 0
        while i<len(l)-1:
            if l[i][1]==l[i+1][1]:
                l[i][0]+=l[i+1][0]
                del l[i+1]
                i-=1
            i+=1
        for x in l:
            f.append(str(x[0])+" "+x[1])
        return f
