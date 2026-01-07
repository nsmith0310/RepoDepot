class Solution:
    def defangIPaddr(self, address: str) -> str:
        s = address
        i = 0
        s2=''
        while i<len(s):
            if s[i]=='.':
                s2+='[.]'
            else:
                s2+=s[i]
            i+=1
        return s2
