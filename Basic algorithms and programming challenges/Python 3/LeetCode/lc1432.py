class Solution:
    def maxDiff(self, num: int) -> int:
        
        num2 = list(str(num))
        
        arr = []
        
        i = 0
        while i<=9:
            j = 0
            while j<=9:
                k = [x for x in num2]
                if str(j) in k:
                    a = 0
                    while a<len(k):
                        if k[a]==str(j): k[a]=str(i)
                        a+=1
                    
                    if k[0]!='0':
                        arr.append(int(''.join(k)))
                j+=1
            i+=1
        return max(arr)-min(arr)
