class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A=="":
            if B=="":
                return True
            else:
                return False
        if B=="":
            if A=="":
                return True
            else:
                return False
        if len(A)!=len(B):
            return False
        if len(A)==1:
            if A!=B:
                return False
        i=1
        while i<len(A):
            tmp = A[1:]+A[0]
            if tmp==B:
                return True
            A=tmp
            i+=1
        return False
