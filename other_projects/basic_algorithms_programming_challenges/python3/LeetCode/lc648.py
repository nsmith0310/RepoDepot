class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        l = sentence.split(" ")
        d = dict
        d.sort()
        
        i = 0
        while i<len(d):
            j = 0
            while j<len(l):
                if d[i] in l[j]:
                    k = len(d[i])
                    if l[j][:k]==d[i]:
                        l[j]=d[i]
                j+=1
            i+=1
        s = ""
        for x in l:
            s+=x+" "
        return s[:-1]
