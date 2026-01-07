class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        l = [[] for i in range(0,max(groupSizes))]
        l2 = []
        
        i = 0
        while i<len(groupSizes):
            l[groupSizes[i]-1].append([i,groupSizes[i]])
            i+=1
        print(l)
        i = 0
        while i<len(l):
            if len(l[i])>0:
                
                tmp = []
                while len(l[i])>0:
                    if len(l[i])==1 and l[i][0][1]!=1:
                        
                        tmp.append(l[i][0][0])
                        l2.append(tmp)
                        del l[i][0]
                    elif len(l[i])==1 and l[i][0][1]==1:
                        if tmp!=[]:
                            l2.append(tmp)
                        l2.append([l[i][0][0]])
                        del l[i][0]
                    elif len(tmp)<l[i][0][1]:
                        tmp.append(l[i][0][0])
                        del l[i][0]
                    else:
                        
                        l2.append(tmp)
                        tmp = []
            i+=1
        return l2
                
                
                    
                
        
