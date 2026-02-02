class Solution:
    def remove(self, s: str) -> str:
        k = list(s)
        i = 0
        while i<len(k)-1:
            if k[i]==k[i+1]:
                del k[i]
                del k[i]
            i+=1
    
        return ''.join(k)
    
    def removeDuplicates(self, S: str) -> str:
        if len(S)<2:
            return S
        l1=S
        l2=""
        while 1!=-1:
            
            l2 = self.remove(l1)
            if l1==l2:
                break
            else:
                l1 = l2
        return l2
            
                    
