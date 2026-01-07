class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l1 = list(map(int,list(str(n))))
        t=1
        for x in l1:
            t*=x
        return t-sum(l1)
