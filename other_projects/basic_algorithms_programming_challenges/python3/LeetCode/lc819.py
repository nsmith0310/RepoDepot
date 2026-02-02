
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punc = [".",",",'"',"'","?","!","$",'`',":",";"]
        s=""
        i = 0 
        while i<len(paragraph):
            if paragraph[i] in punc:
               s+=" "
            else:
                s+=paragraph[i]
            i+=1
            
        l4=s.split(" ")
        l2=[]
        l6=[]
        print(l4,s)
        for x in l4:
            if x!="":
                l6.append(x)
        
        for x in l6:
            l2.append(x.lower())
        
        l3 = banned
        l=[]
        i = 0
        while i<len(l2):
            if l2[i] not in banned:
                l.append(l2[i])
            i+=1
        l5=list(set(l))
        mx = 0
        i = 0
        while i<len(l5):
            if l.count(l5[i])>mx:
                mx = l.count(l5[i])
                r = l5[i]
            i+=1
        return r
        
