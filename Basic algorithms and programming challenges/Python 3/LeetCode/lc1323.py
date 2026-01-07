class Solution:
    def maximum69Number (self, num: int) -> int:
        l = list(str(num))
        if l.count(l[0])==len(l) and l[0]=='9':
            return num
        s = str(num)
        
        i = 0
        while i<len(l):
            if l[i]=='6':
                l[i]='9'
                break
            i+=1
        return int(''.join(l))
