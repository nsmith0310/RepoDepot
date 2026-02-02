class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        l = A
        l2=[]
        for x in l:
            tmp = x[::-1]
            tmp2 = []
            for y in tmp:
                if y==0:
                    tmp2.append(1)
                else:
                    tmp2.append(0)
            l2.append(tmp2)
        return l2
