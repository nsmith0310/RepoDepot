class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n==0:
            return [0]
        tmp=[]
        if n&1==True:
            i = 1
            while i<n:
                tmp.append(i)
                tmp.append(-i)
                i+=2
            tmp.append(0)
        else:
            i = 1
            while i<n:
                tmp.append(i)
                tmp.append(-i)
                i+=2
        return tmp
