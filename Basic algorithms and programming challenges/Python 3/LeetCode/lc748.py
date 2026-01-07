class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        chars = licensePlate.lower()
        
        valid = []
        i = 0
        while i<len(chars):
            if ord(chars[i])-97 >=0 and ord(chars[i])-97 <=25:
                valid.append(chars[i])
            i+=1
        count = []
        v = list(set(valid))
        for x in v:
            count.append([x,chars.count(x)])
        
        mn = 1001
        
        for x in words:
            t = 0
            for y in count:
                if y[1]>x.count(y[0]):
                    t = 1
                    break
            if t==0:
                if len(x)<mn:
                    mn = len(x)
                    f = x
        return f
