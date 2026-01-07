class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        l1 = A.split(" ")
        l2 = B.split(" ")
        l3=[]
        for x in l1:
            if l1.count(x)==1 and x not in l2:
                l3.append(x)
        for x in l2:
            if l2.count(x)==1 and x not in l1:
                l3.append(x)
        return l3
