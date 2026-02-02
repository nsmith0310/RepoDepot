class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        
        
        lim = len(values)
        elem = [[values[i],labels[i]] for i in range(0,lim)]
        
        elem.sort(key=lambda x: x[0])
        elem = elem[::-1]
        
        d = dict()
        for x in elem:
            d[x[1]]=use_limit
            
        t = 0
        count = 0
        for i in range(0,lim):
            if d[elem[i][1]]>0 and count<num_wanted:
                
                t+=elem[i][0]
                d[elem[i][1]]-=1
                count+=1
        return t
                
        
        
