from math import log,floor
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        if bound!=0:
            if x!=1:
                bx = floor(log(bound,x))
            else:
                bx = 1
            if y!=1:
                by = floor(log(bound,y))
            else:
                by = 1
        else:
            return []
        l = []
        i = 0
        j = 0
        while i<=bx:
            j = 0
            while j<=by:
                num = x**i + y**j
                if  num<=bound:
                    l.append(num)
                else:
                    break
                j+=1
            i+=1
        return list(set(l))
