class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        k = list(map(str,A))
        l = []
        i = 1
        f=[]
        while i<=len(k):
            tmp=''.join(k[:i])
            tmp2=int(tmp,2)
            l.append(tmp2)
            i+=1
        for x in l:
            f.append(x%5==0)
        return f
