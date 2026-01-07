class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        l = []
        
        for i in range(lo,hi+1):
            tmp = i
            c=0
            while i!=1:
                c+=1
                if i&1==True:
                    i=3*i + 1
                else:
                    i//=2
            l.append([c,tmp])
        l.sort(key=lambda x: x[0])
        f = []
        for x in l:
            f.append(x[1])
        return f[k-1]
