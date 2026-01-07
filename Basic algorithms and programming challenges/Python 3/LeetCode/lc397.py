class Solution:
    def integerReplacement(self, n: int) -> int:
        if n==1:return 0
        c = 0
        tmp = [n]
        while 1!=-1:
            tmp2=[]
            
            for x in tmp:
                if x==1:
                    return c
                if x%2!=0:
                    tmp2.append(x+1)
                    tmp2.append(x-1)
                else:
                    tmp2.append(x//2)
            c+=1
            tmp = tmp2
