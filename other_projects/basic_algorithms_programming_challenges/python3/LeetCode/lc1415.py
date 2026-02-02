from itertools import product as p

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        l = list(p(['a','b','c'],repeat = n))
        
        c=0
        for x in l:
            tmp = ''.join(x)
            if 'aa' not in tmp and 'bb' not in tmp and 'cc' not in tmp:
                c+=1
                if c==k: return tmp
        return ''
