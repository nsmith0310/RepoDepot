class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if ops==[]:return m*n
        i = m
        j = n
        
        for x in ops:
            if x[0]<i:i=x[0]
            if x[1]<j:j=x[1]
        return i*j
