class Solution:
    def maxProduct(self, words: List[str]) -> int:
        l = list(set(words))
        
        
        l2 = []
        
        
        for x in l:
            l2.append([len(x),set(x)])
        l2.sort(key=lambda x: x[0])
        l2 = l2[::-1]
        mx=0
        i = 0
        while i<len(l2)-1:
            j = i+1
            while j<len(l2):
                s1 = list(l2[i][1]-l2[j][1])
                s2 = list(l2[i][1])
                s1.sort()
                s2.sort()
                
                if s1==s2:
                    
                    pos =  l2[i][0]*l2[j][0]
                    if pos>mx:mx = pos
                j+=1
            i+=1
        return mx
        
        
        
