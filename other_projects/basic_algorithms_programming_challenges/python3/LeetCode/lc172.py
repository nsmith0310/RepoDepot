class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n<5:
            return 0
        f = []
        i = 0
        while pow(5,i)<=n:
            x = n//pow(5,i)
            f.append(x)
            i+=1
        
        return sum(f[1:])
