class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if len(list1)>len(list2):
            short = list2
            long = list1
        else:
            short = list1
            long= list2
            
        pos = []
        
        i = 0
        while i<len(short):
            if short[i] in long:
                pos.append([i+long.index(short[i]),short[i]])
            i+=1
            
        mn=10**6
        
        x = sorted(pos)
        final=[]
        
        for y in x:
            if y[0]<mn:
                mn=y[0]
        for y in x:
            if y[0]==mn:
                final.append(y[1])
        
        
        
        return final
