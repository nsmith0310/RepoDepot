class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        i = 1
        while 1!=-1:
            s1 = str(i)
            s2 = str(n-i)
            if not '0' in s1 and not '0' in s2:
                return [int(s1),int(s2)]
            else:
                i+=1
