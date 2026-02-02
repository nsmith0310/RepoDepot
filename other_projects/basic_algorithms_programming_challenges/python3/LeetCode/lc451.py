class Solution:
    def frequencySort(self, s: str) -> str:
        l = list(set(s))
        l2 = [[x,s.count(x)] for x in l]
        
        l2.sort(key=lambda x: x[1])
        l2 = l2[::-1]
        
        s=""
        for x in l2:
            c = 1
            while c<=x[1]:
                s+=x[0]
                c+=1
        return s
