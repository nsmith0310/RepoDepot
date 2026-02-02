class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        
        l = [n]
        
        s = list(map(int,list(str(n))))
        
        while 1==1:
            num = sum([i**2 for i in s])
            if num==1:
                return True
            elif num in l:
                return False
            else:
                l.append(num)
            s = list(map(int,list(str(num))))
