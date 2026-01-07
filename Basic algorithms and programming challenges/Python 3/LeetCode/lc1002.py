class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        final = []
        i = 0
        a = [list(x) for x in A]
        
        i = 0
        while i<len(a[0]):
            c = 1
            j = 1
            while j<len(a):
                if a[0][i] in a[j]:
                    c+=1
                    del a[j][a[j].index(a[0][i])]
                j+=1
            if c==len(A):
                final.append(a[0][i])
            i+=1
        return final
            
