class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        f = []
        lim = len(str(high))
        
        tmp = [str(i+1) for i in range(0,9)]
        
        s = ''.join(tmp)
        
        i = 0
        while i<len(s)-1:
            j = i+1
            while j<len(s):
                tmp = int(s[i:j+1])
                if tmp>=low and tmp<=high:
                    f.append(tmp)
                j+=1
            i+=1
        f.sort()
        return f
        
