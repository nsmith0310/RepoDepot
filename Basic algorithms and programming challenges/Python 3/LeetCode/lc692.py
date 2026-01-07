class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        b = list(set(words))
        
        
        d = dict()
        
        
        f = []
        l2 = []
        for x in b:
            l2.append([x,words.count(x)])
            
        l2.sort(key=lambda x: x[1])
        
        l2 = l2[::-1]
        
        tmp = []
        
        for x in l2:
            try:
                d[x[1]].append(x[0])
            except:
                d[x[1]]=[x[0]]
                
        for x in d:
            b = d.get(x)
            b.sort()
            for y in b:
                f.append(y)
        return f[:k]
        
        
