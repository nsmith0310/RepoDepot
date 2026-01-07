class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        n = len(A)//2
        l = list(set(A))
        for x in l:
            if A.count(x)==n:
                return x
