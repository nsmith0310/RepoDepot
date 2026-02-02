class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        if K==0:
            return max(A)-min(A)
        A.sort()
        n1 = min(A)+abs(K)
        n2 = max(A)-abs(K)
        if n1>=n2:
            return 0
        else:
            return abs(n2-n1)
