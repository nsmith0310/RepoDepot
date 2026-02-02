class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        l = []
        i = 0
        while i<len(widths):
            l.append([alph[i],widths[i]])
            i+=1
        l2=[[]]
        i=0
        count = 100
        while i<len(S):
            length = l[alph.index(S[i])][1]
            if count-length>=0:
                count-=length
                l2[-1].append(length)
            else:
                count = 100-length
                l2.append([length])
            i+=1
            
        return [len(l2),sum(l2[-1])]
            
            
