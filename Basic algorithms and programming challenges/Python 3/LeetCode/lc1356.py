class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        if len(list(set(arr)))==1:
            return arr
        l1 = [[str(bin(x))[2:],x] for x in arr]
        l2=[]
        for x in l1:
            l2.append([x[0].count('1'),x[1]])
        l3 = sorted(l2)
        
        l4=[]
        i = 0
        final=[]
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
                    
        return final
        
