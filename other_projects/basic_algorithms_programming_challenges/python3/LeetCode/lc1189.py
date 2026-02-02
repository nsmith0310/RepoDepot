class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        l = []
        l.append(text.count('b'))
        l.append(text.count('a'))
        l.append(text.count('l'))
        l.append(text.count('o'))
        l.append(text.count('n'))
        if 0 in l:
            return 0
        if l[2] <2 or l[3] <2:
            return 0
        dbl = min([l[2]//2,l[3]//2])
        
        b = l[0]
        a = l[1]
        n = l[4]
        sing = min([b,a,n])
        
        if sing<=dbl:
            return sing
        else:
            return dbl
            
            
