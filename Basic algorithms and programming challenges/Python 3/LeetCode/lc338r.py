class Solution:
    def countBits(self, num: int) -> List[int]:
        l=[]
        i = 0
        while i<=num:
            l.append((str(bin(i))[2:]).count('1'))
            i+=1
        return l
