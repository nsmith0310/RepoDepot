class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        elif strs==[]:
            return ""
        
        mn = 999999999
        
        start = ""
        i = 0
        while i<len(strs):
            if len(strs[i])<mn:
                mn = len(strs[i])
                start = strs[i]
                
            i+=1
        f=""
        i = 0
        while i<len(start):
            tmp = [x[i] for x in strs]
            if len(list(set(tmp)))==1:
                f+=start[i]
            else:
                break
            i+=1
        return f
                
        
        
