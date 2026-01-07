class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        if "." in version1:
            l1 = version1.split(".")
        else:
            l1 = [version1]
        if "." in version2:
            l2 = version2.split(".")
        else:
            l2 = [version2]
            
        while len(l2)<len(l1):
            l2.append("0")
        while len(l1)<len(l2):
            l1.append("0")
            
        a = list(map(int,(l1)))
        b = list(map(int,(l2)))
        
        
        i = 0
        while i<len(a):
            if a[i]>b[i]:return 1
            if b[i]>a[i]:return -1
            i+=1
        return 0
        
        
