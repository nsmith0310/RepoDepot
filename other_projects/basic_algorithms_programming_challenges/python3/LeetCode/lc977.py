class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        l = [i**2 for i in A]
        l.sort()
        return l
