class Solution:
    def arrangeWords(self, text: str) -> str:
        
        s = text.lower()
        l = s.split(" ")
        
        l2 = [[x,len(x)] for x in l]
        
        l2.sort(key=lambda x: x[1])
        
        w1 = l2[0][0]
        up = w1[0].upper()
        w1 = up+w1[1:]
        l2[0][0]=w1
        
        return(' '. join([x[0] for x in l2]))
