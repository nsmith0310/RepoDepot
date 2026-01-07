class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l = mat
        l2 = []
        i = 0
        while i<len(l):
            l2.append([l[i].count(1),i])
            i+=1
        l3 = sorted(l2)
        
        final=[]
        i=0
        while i<len(l3):
            tmp = []
            j = i
            while j<len(l3):
                if l3[i][0]==l3[j][0]:
                    tmp.append(l3[j][1])
                    i=j
                j+=1
            
            for x in tmp:
                final.append(x)
            ###print(final)
            i+=1
        return final[:k]
