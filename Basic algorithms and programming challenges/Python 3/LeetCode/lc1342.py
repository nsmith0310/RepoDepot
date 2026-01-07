class Solution:
    def numberOfSteps (self, num: int) -> int:
        i = 0
        if num==0:
            return 0
        while num!=0:
            if num&1==True:
                num-=1
                i+=1
            else:
                num//=2
                i+=1
        return i
