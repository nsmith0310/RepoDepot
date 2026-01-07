class Solution:
    def isValid(self, s: str) -> bool:
        l = list(s)
        k = 0
        while k==0:
            a = 0
            b = 0
            c = 0
            if "[]" in s:
                a = 1
                while "[]" in s:
                    ind = s.index("[]")
                    del l[ind:ind+2]
                    s=''.join(l)
                    l = list(s)   
            if "{}" in s:
                b = 1
                while "{}" in s:
                    ind = s.index("{}")
                    del l[ind:ind+2]
                    s=''.join(l)
                    l = list(s)    
            if "()" in s:
                c = 1
                while "()" in s:
                    ind = s.index("()")
                    del l[ind:ind+2]
                    s=''.join(l)
                    l = list(s)
            if a==0==b==c:
                break
        
        return s==""
