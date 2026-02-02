class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if len(pairs)<2:
            return 0
        pairs.sort(key=lambda x: x[1])
        
        
        i = 0
        while i<len(pairs)-1:
            if pairs[i][1]>=pairs[i+1][0]:
                del pairs[i+1]
                i-=1
            i+=1
        
        
        
        mx = 0
        i = 0
        c = 1
        while i<len(pairs)-1:
            if pairs[i][1]<pairs[i+1][0]:
                c+=1
                if c>mx:
                    mx = c
            else:
                c=1
            i+=1
        if mx==0:
            return 1
        else:
            return mx
