class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        e = []
        o = []
        for x in A:
            if x&1==True:
                o.append(x)
            else:
                e.append(x)
        for x in o:
            e.append(x)
        return e
