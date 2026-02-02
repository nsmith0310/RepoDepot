class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        d = dict()
        count = dict()
        i = 0
        while i<len(paths):
            
            j = 0
            while paths[i][j]!=" ":
                j+=1
            path = paths[i][:j]
            paths[i]=paths[i][j+1:]
            proc = paths[i].split(" ")
            for x in proc:
                
                j = len(x)-1
                k = j
                while x[j]!="(":
                    j-=1
                s = x[j+1:k]
                try:
                    d[s].append(path+"/"+x[:j])
                    count[s]+=1
                except:
                    d[s]=[path+"/"+x[:j]]
                    count[s]=1
            i+=1
        f = []
        for x in d:
            if count[x]>1:
                f.append(d.get(x))
        return f
