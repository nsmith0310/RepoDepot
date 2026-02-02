class Solution:
    def validIPAddress(self, IP: str) -> str:
        if ("." in IP and ":" in IP) or " " in IP:return "Neither"
        ipv4 = ['0','1','2','3','4','5','6','7','8','9','.']
        ipv6 = ['0','1','2','3','4','5','6','7','8','9',':','a','b','c','d','e','f']
        
        if "." in IP:
            i = 0
            while i<len(IP):
                if IP[i] not in ipv4:
                    return "Neither"
                i+=1
            if IP[-1]=="." or IP[0]=="." or IP.count(".")!=3: return "Neither"
            
            i = 0
            while i<len(IP)-1:
                if IP[i]+IP[i+1]=="..": return "Neither"
                i+=1
                
                
            
            s = IP.split(".")
            
            if len(s)!=4:
                return "Neither"
            for x in s:
                if (x[0]=="0" and len(x)>1) or int(x)>255:
                    return "Neither"
            return "IPv4"
        
        elif ":" in IP:
            IP = IP.lower()
            i = 0
            while i<len(IP):
                if IP[i] not in ipv6:
                    return "Neither"
                i+=1
                
            if "::" in IP or IP[-1]==":": return "Neither"
            s = IP.split(":")
            if len(s)!=8 or s[-1]==":": return "Neither"
            
            for x in s:
                if len(x)>4 and x[0]=='0': return "Neither"
                if len(x)>4: return "Neither"
                    
            return "IPv6"
            
        else: return "Neither"
