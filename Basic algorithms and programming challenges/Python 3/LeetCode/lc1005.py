class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        while K>0:
            i = min(A)
            A[A.index(i)]*=-1
            K-=1
        return sum(A)
