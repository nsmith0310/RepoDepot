class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc = [x for x in A]
        dec = [x for x in A]
        
        inc.sort()
        dec.sort(reverse=True)
        if inc==A:
            return True
        if dec==A:
            return True
        return False
