class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        s1 = list(J)
        s2 = S
        c=0
        for x in s1:
            c+=s2.count(x)
        return c
