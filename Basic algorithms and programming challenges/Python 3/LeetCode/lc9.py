class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if len(s)&1==True:
            s1 = (len(s)//2)
            s2 = (len(s)//2)+1
            sub1 = s[:s1]
            sub2 = s[s2:][::-1]
            print(sub1,sub2)
            return sub1==sub2
        else:
            s1 = (len(s)//2)
            s2 = (len(s)//2)
            sub1 = s[:s1]
            sub2 = s[s2:][::-1]
            print(sub1==sub2)
            return sub1==sub2
